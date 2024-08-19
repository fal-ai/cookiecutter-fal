VENV_PIP := .venv/bin/pip
VENV_PY := .venv/bin/python

APP_LOC := src/{{ cookiecutter.project_slug }}/inference.py::{{ cookiecutter.app_class_name }}
APP_NAME := {{ cookiecutter.app_name }}
APP_KEEP_ALIVE := {{ cookiecutter.keep_alive }}

PYTHON_BIN_PATH := $(shell which python{{ cookiecutter.python_version }})

init:
	${VENV_PIP} install --upgrade pip
	${VENV_PIP} install--upgrade virtualenv setuptools
	${PYTHON_BIN_PATH} -m virtualenv .venv -p ${PYTHON_BIN_PATH}
	${VENV_PIP} install -e '.[dev]'
	${VENV_PY} -m pre_commit install

run:
	${VENV_PY} -m fal run ${APP_LOC}

deploy:
	${VENV_PY} -m fal apps scale ${APP_NAME} --keep-alive=${APP_KEEP_ALIVE}
	${VENV_PY} -m fal deploy ${APP_LOC}

test:
	${VENV_PY} -m pytest -vvv tests/ -sss
