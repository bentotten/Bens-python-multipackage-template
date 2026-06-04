# Development

## Table of Contents

- [Environment Setup](#environment-setup)
- [Running Checks](#running-checks)
- [Cleaning](#cleaning)
- [Windows](#windows-note)

## Environment Setup and Build

Create and activate the environment:

```bash
micromamba create -f environment.yaml
micromamba activate behavior-similarity-search
```

Then install the project:

```bash
make build
```

To deactivate:

```bash
micromamba deactivate
```

## Running Checks

| Command                | Description                                      |
|------------------------|--------------------------------------------------|
| `make build`           | Install the project and dev dependencies         |
| `make lint`            | Check for code quality issues with ruff          |
| `make check-codestyle` | Check formatting without making changes          |
| `make type-check`      | Run static type checking with mypy               |
| `make test`            | Run the test suite with pytest                   |
| `make format`          | Auto-fix lint and formatting issues (local only) |
| `make ci`              | Run all checks in sequence (mirrors CI)          |

## Cleaning

| Command            | Description                                    |
|--------------------|------------------------------------------------|
| `make clean`       | Remove all build, pyc, and test artifacts      |
| `make clean-build` | Remove build artifacts                         |
| `make clean-pyc`   | Remove compiled Python files and `__pycache__` |
| `make clean-test`  | Remove test and coverage artifacts             |
| `make clean-docs`  | Remove generated documentation                 |


## Windows Note

**Note:** This project uses `make` and bash tooling which are not natively available on Windows. The recommended approach is to use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux), which provides a full Linux environment.

Install WSL2 with Ubuntu from PowerShell:

```powershell
wsl --install
```

Then follow the rest of the setup instructions inside the WSL2 terminal.