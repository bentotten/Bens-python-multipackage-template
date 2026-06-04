"""Integration tests — cross-package interactions."""

from my_core.main import run
from my_cli.cli import main


def test_core_and_cli_importable() -> None:
    """Test that both packages can be imported together."""
    assert callable(run)
    assert callable(main)
