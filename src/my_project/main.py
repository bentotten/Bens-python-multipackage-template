"""Entry point for MyProject."""

from my_project import __version__


def run() -> None:
    """Run the application.

    Prints the current version of the package to stdout.
    """
    print(f"MyProject v{__version__}")


if __name__ == "__main__":
    run()
