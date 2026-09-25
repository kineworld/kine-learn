"""Fail if the standard runner cannot see every test in this directory.

**This is the organisation-level copy.** Drop it into a repository's test directory and
call it from CI -- that is exactly what ``.github/workflows/python-tests.yml`` in this
repository expects to find, and it refuses to run a suite without it. The directory does
not have to be called ``tests``: it is wherever this file sat down, which is how a
repository whose suite lives in ``world-models/labs/`` is covered as well.

Why it exists: four self-authored repositories in this organisation hold test functions
that no job will ever execute, in three different shapes (no workflow at all; a workflow
that runs one named module instead of discovering; a suite whose tests the loader cannot
see). The audit is in kineworld/.github#3.

Why it derives the expected count with :mod:`ast` instead of storing a number: a
hand-maintained count drifts out of date and then silently stops checking, which is the
same class of mistake as the defect this guards against.

    python path/to/tests/check_collection.py
"""

import ast
import pathlib
import sys
import unittest

TESTS_DIR = pathlib.Path(__file__).resolve().parent


def find_repo_root(start):
    """Walk up to the directory holding ``.git``.

    Not simply ``start.parent``: this file may sit in a test directory that is not
    directly under the repository root (``world-models/labs/`` in kineworld/.github is
    one), and the import path has to be the repository root wherever the suite lives.
    """
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return start.parent


REPO_ROOT = find_repo_root(TESTS_DIR)
DIR_NAME = TESTS_DIR.name


def count_tests_in(path):
    """Return the number of test functions a file appears to define."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    count = 0
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith("test_"):
                count += 1
        elif isinstance(node, ast.ClassDef):
            for inner in node.body:
                if isinstance(inner, ast.FunctionDef) and inner.name.startswith("test_"):
                    count += 1
    return count


def discover():
    """Collect the suite the same way CI does, for this layout.

    A package directory (one with ``__init__.py``) must be discovered with an explicit
    top-level directory; without one, ``discover`` treats it as a set of top-level
    modules, never imports it as a package, and a package-level ``load_tests`` would not
    run. A plain directory must be discovered WITHOUT a top-level directory, because
    ``discover`` raises ``ImportError`` when the start directory is not importable.

    Repositories that keep every test inside a ``TestCase`` have no ``__init__.py`` and
    are fine either way; this picks the form their CI would use, and
    ``.github/workflows/python-tests.yml`` branches on the same rule so that the guard
    and the run never disagree about what "collected" means.
    """
    if (TESTS_DIR / "__init__.py").exists():
        return unittest.TestLoader().discover(str(TESTS_DIR), top_level_dir=str(REPO_ROOT))
    return unittest.TestLoader().discover(str(TESTS_DIR))


def main():
    files = sorted(TESTS_DIR.glob("test_*.py"))
    if not files:
        raise SystemExit("no test_*.py files found in %s/" % DIR_NAME)

    expected = sum(count_tests_in(f) for f in files)

    sys.path.insert(0, str(REPO_ROOT))
    collected = discover().countTestCases()

    print("%d test files in %s/ | %d test functions in source | %d collected by unittest"
          % (len(files), DIR_NAME, expected, collected))

    if collected != expected:
        # Both directions, because only one of them used to be described. When the runner
        # collects MORE than the source defines the old message printed a negative count
        # ("-1 invisible"), which is not a thing.
        if collected < expected:
            detail = ("%d test function(s) here are not collected by the runner, so they can "
                      "never fail. If they are written as module-level functions, "
                      "guards/load_tests.py in kineworld/.github is the fix."
                      % (expected - collected))
        else:
            detail = ("the runner collected %d more test(s) than the source defines. Usually "
                      "that is a name imported into a test module rather than defined in it, or "
                      "a definition in a place ast does not count -- a function under an `if` "
                      "at module level, for instance." % (collected - expected))
        raise SystemExit(
            "the runner collected %d tests but the source defines %d. %s "
            "This also fires when a test module cannot be imported at all, which is a "
            "different fix entirely -- run the suite to see the import error."
            % (collected, expected, detail)
        )

    print("ok: every test in %s/ is visible to the runner" % DIR_NAME)


if __name__ == "__main__":
    main()
