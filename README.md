# Geo Location

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

get location from user

## Overview

This project was generated using
[SolarEdge Python Package Template](http://gitlab-ng.solaredge.local/solaredge-shared-source/projectk8s/solaredge-python-package-template).

To create new projects, use [SolarEdge Initializer](http://initializer.solaredge.local).

**We encourage users to edit this README with their own content.**

## Generation Parameters
The following parameters were used to generate this project:

```json
{
    "project_slug": "geo-location",
    "project_description": "get location from user",
    "package_name": "trading-bot",
    "package_title": "Geo Location",
    "project_maintainer": "tomer.gur@solaredge.com",
    "publish_as_package": "True",
    "solaredge_group": "home-automation",
    "_template": "git@gitlab-ng.solaredge.local:solaredge-shared-source/projectk8s/solaredge-python-package-template.git"
    
}
```

## Getting Started
### Installation
You can install this package from Home Automation's PyPi repository like so:

```shell
pip install geo-location -i http://docker-esh.solaredge.com/artifactory/api/pypi/home-automation-pypi/simple
```

If your project uses Poetry, you need to first add Home Automation's PyPi repository like so:

```shell
poetry config repositories.iotp-pypi http://docker-esh.solaredge.com/artifactory/api/pypi/home-automation-pypi/simple
```

Than you can add the package as you normally would:

```shell
poetry add geo-location
```

### Dependencies
The package requires Python 3.9 or higher to get started, and has several dependencies which are specified in `pyproject.toml`.

## Contributor's Guide
The project uses a Makefile to manage common tasks. Here are the available targets:

- `make`, `make all` - Runs the `check` target
- `make check` - Runs Pylint and Mypy static analysis, as well as all pre-commit hooks
- `make test` - Runs tests using pytest
- `make coverage` - Runs tests using pytest and reports test coverage
- `make pylint` - Runs pylint
- `make mypy` - Runs mypy
- `make package` - Creates a Python package that can be deployed to a PyPI repository
- `make bootstrap` - Creates a virtualenv and installs all dependencies
- `make prune` - Deletes the virtualenv

### Poetry
The project uses [Poetry](https://python-poetry.org/) to build the package and manage dependencies.

If you're not familiar with Poetry, read the documentation.

### PreCommit
The project uses [Pre-Commit](https://pre-commit.com/) to automatically run git hooks that verify
proper formatting, type safety, etc.

After cloning this project, you should run `pre-commit install` to enable pre-commit. This would help you
automatically run all hooks when committing, thus finding failures locally and quickly - instead of during
gitlab pipelines.
