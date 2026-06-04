"""Unit tests for my_core."""

import my_core
from my_core import __version__
from my_core.main import run


def test_package_importable() -> None:
    """Test that my_core is importable."""
    assert my_core is not None


def test_version_defined() -> None:
    """Test that __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_run_importable() -> None:
    """Test that run() is importable and callable."""
    assert callable(run)
