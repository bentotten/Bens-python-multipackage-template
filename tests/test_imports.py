"""Basic import tests to verify the package structure is intact."""

import my_project
from my_project import __version__
from my_project.main import run


def test_package_importable() -> None:
    """Test that the top-level package is importable."""
    assert my_project is not None


def test_version_defined() -> None:
    """Test that __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_run_importable() -> None:
    """Test that the run() entry point is importable and callable."""
    assert callable(run)
