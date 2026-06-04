# BehaviorSimilaritySearch
A computer vision project to detect if specific behaviours are present in video segments.

## Table of Contents

- [Prerequisites](#prerequisites)
    - [Note for Windows users](#note-for-windows-users)
    - [micromamba](#micromamba)
- [Installation](#installation)

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
