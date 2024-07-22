import subprocess

PYTHON_VERSION = "{{ cookiecutter.python_version }}"
PYTHON_BINARY = (
    subprocess.check_output(["which", f"python{PYTHON_VERSION}"]).decode().strip()
)

subprocess.check_call(
    [PYTHON_BINARY, "-m", "pip", "install", "--upgrade", "pip", "setuptools"]
)

subprocess.check_call(
    [PYTHON_BINARY, "-m", "pip", "install", "pre-commit", "black", "isort"]
)

subprocess.check_call([PYTHON_BINARY, "-m", "black", "."])

subprocess.check_call(
    [
        PYTHON_BINARY,
        "-m",
        "isort",
        "--profile=black",
        ".",
    ],
)


subprocess.check_call(["git", "init"])
subprocess.check_call(
    [PYTHON_BINARY, "-m", "pre_commit", "install", "--install-hooks"],
    cwd="{{ cookiecutter.project_slug }}",
)
subprocess.check_call(
    [PYTHON_BINARY, "-m", "pre_commit", "autoupdate"],
    cwd="{{ cookiecutter.project_slug }}",
)
subprocess.check_call(["git", "add", "--all"])
subprocess.check_call(
    ["git", "commit", "-m", "Add initial project."],
    cwd="{{ cookiecutter.project_slug }}",
)
subprocess.check_call(
    ["git", "tag", "v0.0.1"],
    cwd="{{ cookiecutter.project_slug }}",
)
subprocess.check_call(
    ["git", "branch", "-M", "main"],
    cwd="{{ cookiecutter.project_slug }}",
)
