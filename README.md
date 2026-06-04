# MyProject

A template for multi-package python project consisting of my favorite setups. This is set up so that each subpackage can be installed and deployed independently, allowing for independent edge and cloud deployments without bloating dependencies.

## Table of Contents

- [Prerequisites](#prerequisites)
    - [Note for Windows users](#note-for-windows-users)
    - [micromamba](#micromamba)
- [Installation](#installation)
- [Deploying Packages Independently](#deploying-packages-independently)

## Prerequisites


### Note for Windows users

This project uses `make` and bash tooling which are not natively available on Windows. The recommended approach is to use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux), which provides a full Linux environment.

Install WSL2 with Ubuntu from PowerShell:

```powershell
wsl --install
```

Then follow the standard Linux setup instructions inside the WSL2 terminal.

### micromamba

This project uses [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) to manage the environment.

**Linux, macOS, or Git Bash on Windows:**

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

**macOS (Homebrew):**

```bash
brew install micromamba
```

**Windows (PowerShell):**

```powershell
Invoke-Expression ((Invoke-WebRequest -Uri https://micro.mamba.pm/install.ps1 -UseBasicParsing).Content)
```

Once installed, micromamba can be updated at any time with:

```bash
micromamba self-update
```

## Installation

Create and activate the environment:

```bash
micromamba create -f environment.yaml
micromamba activate my-project
```

Then install the project:

```bash
make build
```

To run:

```bash
cli
```

To deactivate:

```bash
micromamba deactivate
```

## Deploying Packages Independently

Each sub-package has its own `pyproject.toml` and can be installed on its own, without pulling in the entire repository. This allows different parts of the project to run on different devices or instances with only the dependencies they need.

```bash
# Core library only
uv pip install -e "packages/my_library"

# Application
uv pip install -e "apps/my_app"
```
