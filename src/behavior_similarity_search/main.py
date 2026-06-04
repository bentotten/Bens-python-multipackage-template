"""Entry point for Behavior Similarity Search."""

from behavior_similarity_search import __version__


def run() -> None:
    """Run the application.

    Prints the current version of the package to stdout.
    """
    print(f"Behavior Similarity Search v{__version__}")


if __name__ == "__main__":
    run()
