PACKAGE_NAME := geo_location

# . . . . . . . . . . . . Phony Targets . . . . . . . . . . . . . . . .
.PHONY: all clean bootstrap check test coverage pylint mypy package prune

all: check

check: bootstrap
	poetry run pre-commit run --all-files

test: bootstrap
	poetry run pytest --log-cli-level=4 tests

coverage: bootstrap
	poetry run pytest --cov-report html --cov-report term --cov=. --log-cli-level=4 tests

pylint: bootstrap
	poetry run pylint $(PACKAGE_NAME)

mypy: bootstrap
	poetry run mypy -p $(PACKAGE_NAME)

package: bootstrap
	poetry build

bootstrap: .make.bootstrap

prune:
	rm -rf .make.bootstrap
	rm -rf .venv

# . . . . . Real Targets . . . . .

# We need to reinstall dependencies whenever pyproject.toml is newer than the
# lock file than the one created the last time we bootstrapped.
# We can't use the committed lock file, as it is committed to git and when
# someone pulls it from git it will always seem up to date.
.make.bootstrap: pyproject.toml
	poetry install
	touch .make.bootstrap
