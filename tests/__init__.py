"""Make every ``test_*`` in this directory visible to the standard runner.

**This is the organisation-level copy.** Copy it into a repository's test directory as
``__init__.py``. Together with ``check_collection.py`` from this directory and three lines
of workflow YAML, that is the whole adoption -- see ``guards/README.md``.

Why it exists: ``unittest`` collects ``TestCase`` methods and ignores functions named
``test_*`` that sit at module level. So a test file written to be run directly

    $ python tests/test_windows.py
    PASS test_windows

is invisible to the standard runner

    $ python -m unittest discover -s tests
    Ran 0 tests in 0.000s
    NO TESTS RAN

The file is not broken. The loader cannot see it, and an exit code of 5 next to a green
hand-run is easy to read as "nothing wrong here". Four self-authored repositories in this
organisation hold 47 such functions -- every one of them correct, none of them ever
executed. The audit is in kineworld/.github#3. This module implements the documented
``load_tests`` protocol so they are collected without changing a single test.

Use either of:

    python -m unittest discover -s tests -t .     # note -t .
    python -m unittest tests

``-t .`` is load-bearing. Without a top-level directory, ``discover`` treats the test
directory as a set of top-level modules, never imports it as a package, and this module is
never reached. ``check_collection.py`` and
``kineworld/.github/.github/workflows/python-tests.yml`` both branch on the same rule, so
the guard, the local command and CI always agree on what "collected" means.
"""

import importlib
import inspect
import pkgutil
import unittest


def _named(case_class, name):
    """Name a generated TestCase class after what it stands for.

    On the *class*, not the instance: ``TestCase.id()`` reads the class, so setting
    ``__name__`` on an instance changes nothing and the id comes out as
    ``tests._import_failure.<locals>._ImportFailure.runTest`` -- which names neither the
    module nor the test, and that is the only thing these placeholders exist to do.
    """
    case_class.__name__ = name
    case_class.__qualname__ = name
    return case_class()


def _wrapper(module_name, function_name, function):
    """Return a one-method ``TestCase`` whose only job is to call ``function``."""

    class _BareFunctionTest(unittest.TestCase):
        def runTest(self):  # unittest's own protocol name; it is not misspelled
            function()

    return _named(_BareFunctionTest, "Test_%s_%s" % (module_name, function_name))


def _import_failure(module_name, error):
    """A single failing test standing in for a module that would not import.

    Enumerating modules means importing them, which means this module needs whatever they
    import. A dependency that is missing from the manifest therefore lands here, and
    without this it lands *badly*: importing the package raises, ``discover`` wraps that in
    one ``_FailedTest`` for the package, and the guard reports

        17 test functions in source | 1 collected by unittest

    pointing at "16 invisible tests" when the actual message is "No module named 'numpy'".
    Measured, on kineworld/kine-bench: that is exactly what a torch-only environment
    produced. One placeholder per module keeps the other modules running and puts the real
    exception in the test output, which is also what unittest does for a module it cannot
    import during discovery.
    """

    class _ImportFailure(unittest.TestCase):
        def runTest(self):
            raise error

    return _named(_ImportFailure, "Test_%s_import" % module_name)


def _iter_test_modules():
    """Yield ``(name, module_or_None, error_or_None)`` for every ``test_*.py`` beside this file.

    Enumerated at import time rather than listed in a literal: a file added later must not
    need an edit here. A hand-maintained list drifts, and a drifted list silently stops
    covering the thing it was written to cover -- which is this defect one level up.
    """
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
        if not info.name.startswith("test_"):
            continue
        try:
            yield info.name, importlib.import_module("%s.%s" % (__name__, info.name)), None
        except Exception as error:  # noqa: BLE001 - reported as a failing test, not swallowed
            yield info.name, None, error


def load_tests(loader, tests, pattern):
    """Collect ``TestCase`` classes *and* module-level ``test_*`` functions.

    A package-level ``load_tests`` **replaces** the default collection rather than adding
    to it, so both kinds have to be handled here. Handling only the bare functions drops
    every ``TestCase`` method in the directory -- and still reports success, which is how
    the first attempt at this fix in kineworld/kine-jepa#4 would have quietly removed five
    passing tests.
    """
    suite = unittest.TestSuite()
    for module_name, module, error in _iter_test_modules():
        if error is not None:
            suite.addTest(_import_failure(module_name, error))
            continue
        # 1. TestCase subclasses, through the standard loader, so that the usual rules
        #    (including a module-level load_tests) still apply to them.
        suite.addTests(loader.loadTestsFromModule(module))
        # 2. Module-level test_* functions, which that loader passes over.
        for name, value in sorted(vars(module).items()):
            if not name.startswith("test_") or not inspect.isfunction(value):
                continue
            # Only functions *defined in* the module. ``check_collection.py`` counts
            # top-level ``def test_*`` with ast, and the two numbers have to mean the same
            # thing; an imported name would be collected here and not counted there.
            if value.__name__ != name or value.__module__ != module.__name__:
                continue
            suite.addTest(_wrapper(module_name, name, value))
    return suite
