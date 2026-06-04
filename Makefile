SHELL=/bin/bash
LINT_PATHS = src/ tests/

# ---------------------------------------------------------------
# Cleaning
# ---------------------------------------------------------------

.PHONY: clean clean-build clean-pyc clean-test clean-docs

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	find . -name '.coverage' -exec rm -r {} +
	rm -fr htmlcov/
	rm -fr .pytest_cache/
	rm -fr .mypy_cache/
	rm -fr .ruff_cache/

clean-docs:
	cd docs && make clean
	rm -fr docs/_build

# ---------------------------------------------------------------
# Checks (used in CI)
# ---------------------------------------------------------------

.PHONY: lint check-codestyle type-check test

lint:
	ruff check $(LINT_PATHS)

check-codestyle:
	ruff format --check $(LINT_PATHS)

type-check:
	mypy $(LINT_PATHS)

test:
	pytest tests/

# ---------------------------------------------------------------
# Local convenience
# ---------------------------------------------------------------

.PHONY: format ci build

format:
	ruff check --fix $(LINT_PATHS)
	ruff format $(LINT_PATHS)

# Run all checks (mirrors CI)
ci: lint check-codestyle type-check test

# Build/install the project
build:
	uv pip install -e ".[dev]"
	@echo "Build complete. Run with 'bss'"
