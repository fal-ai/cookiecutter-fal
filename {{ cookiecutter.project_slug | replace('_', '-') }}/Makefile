VENV_PIP := .venv/bin/pip
VENV_PY := .venv/bin/python

APP_LOC := src/{{ cookiecutter.project_slug }}/inference.py::{{ cookiecutter.app_class_name }}
APP_NAME := {{ cookiecutter.app_name }}
APP_KEEP_ALIVE := {{ cookiecutter.keep_alive }}

PYTHON_BIN_PATH := $(shell which python{{ cookiecutter.python_version }})

check-python-{{ cookiecutter.python_version }}:
	@if [ -z "$(PYTHON_{{ cookiecutter.python_version }}_BIN_PATH)" ]; then \
		echo "Error: Python {{ cookiecutter.python_version }} is not installed or not in PATH."; \
		echo "Please install Python {{ cookiecutter.python_version }} and make sure it's available in your PATH."; \
		exit 1; \
	elif ! $(PYTHON_{{ cookiecutter.python_version }}_BIN_PATH) -c "import sys; sys.exit(0)"; then \
		echo "Error: Python {{ cookiecutter.python_version }} is not functioning correctly."; \
		echo "Please ensure Python {{ cookiecutter.python_version }} is properly installed and configured."; \
		exit 1; \
	fi

init: check-python-{{ cookiecutter.python_version }}
	${PYTHON_BIN_PATH} -m pip install --upgrade pip virtualenv
	${PYTHON_BIN_PATH} -m virtualenv .venv -p ${PYTHON_BIN_PATH}
	${VENV_PIP} install --upgrade pip
	${VENV_PIP} install --upgrade virtualenv setuptools
	${VENV_PIP} install -e '.[dev]'
	${VENV_PY} -m pre_commit install

run: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m fal run ${APP_LOC}

deploy: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m fal apps scale ${APP_NAME} --keep-alive=${APP_KEEP_ALIVE}
	${VENV_PY} -m fal deploy ${APP_LOC}

test: check-python-{{ cookiecutter.python_version }}
	${VENV_PY} -m pytest -vvv tests/ -sss
