"""Basic import tests to verify the package structure is intact."""

import behavior_similarity_search
from behavior_similarity_search import __version__
from behavior_similarity_search.main import run


def test_package_importable() -> None:
    """Test that the top-level package is importable."""
    assert behavior_similarity_search is not None


def test_version_defined() -> None:
    """Test that __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_run_importable() -> None:
    """Test that the run() entry point is importable and callable."""
    assert callable(run)
