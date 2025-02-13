VENV_PIP := .venv/bin/pip
VENV_PY := .venv/bin/python

PYTHON_BIN_PATH := $(shell which python{{ cookiecutter.python_version }})

-include .env
export

check-python-{{ cookiecutter.python_version }}:
	@if [ -z "$(PYTHON_BIN_PATH)" ]; then \
		echo "Error: Python {{ cookiecutter.python_version }} is not installed or not in PATH."; \
		echo "Please install Python {{ cookiecutter.python_version }} and make sure it's available in your PATH."; \
		exit 1; \
	elif ! $(PYTHON_BIN_PATH) -c "import sys; sys.exit(0)"; then \
		echo "Error: Python {{ cookiecutter.python_version }} is not functioning correctly."; \
		echo "Please ensure Python {{ cookiecutter.python_version }} is properly installed and configured."; \
		exit 1; \
	fi

init: check-python-{{ cookiecutter.python_version }}
	${PYTHON_BIN_PATH} -m venv .venv
	${VENV_PIP} install --upgrade pip
	${VENV_PIP} install --upgrade setuptools
	${VENV_PIP} install -e '.[dev]'
	${VENV_PY} -m pre_commit install

run: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m fal run {{ cookiecutter.app_name }}

deploy: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m fal deploy {{ cookiecutter.app_name }}

test: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m pytest -vvv tests/ -sss
