VENV_PIP := .venv/bin/pip
VENV_PY := .venv/bin/python

APP_LOC := {{ cookiecutter.project_slug }}/inference.py::{{ cookiecutter.app_class_name }}
APP_NAME := {{ cookiecutter.project_slug.lower() | replace('_', '-') }}
APP_AUTH := {{ cookiecutter.app_auth }}
APP_KEEP_ALIVE := {{ cookiecutter.keep_alive }}

PYTHON_BIN_PATH := $(shell which python{{ cookiecutter.python_version }})

init:
	virtualenv .venv -p ${PYTHON_BIN_PATH}
	${VENV_PIP} install -e .
	${VENV_PIP} install -r requirements-dev.txt

run:
	${VENV_PY} -m fal run ${APP_LOC}

deploy:
	${VENV_PY} -m fal apps scale ${APP_NAME} --keep-alive=${APP_KEEP_ALIVE}
	${VENV_PY} -m fal deploy ${APP_LOC} --app-name ${APP_NAME} --auth ${APP_AUTH}

test:
	${VENV_PY} -m pytest -vvv tests/ -sss