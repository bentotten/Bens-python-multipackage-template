"""Entry point for my_core."""

from my_core import __version__


def run() -> None:
    """Run the application.

    Prints the current version of the package to stdout.
    """
    print(f"MyProject v{__version__}")


if __name__ == "__main__":
    run()
