"""Unit tests for my_cli."""

import argparse

import my_cli
from my_cli import __version__
from my_cli.cli import build_parser, main


def test_package_importable() -> None:
    """Test that my_cli is importable."""
    assert my_cli is not None


def test_version_defined() -> None:
    """Test that __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_build_parser_returns_parser() -> None:
    """Test that build_parser returns an ArgumentParser."""
    parser = build_parser()
    assert isinstance(parser, argparse.ArgumentParser)


def test_main_importable() -> None:
    """Test that main() is importable and callable."""
    assert callable(main)
