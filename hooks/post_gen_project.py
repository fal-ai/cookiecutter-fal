import subprocess

subprocess.run(["black", "."], check=True)

subprocess.run(
    [
        "isort",
        "--profile=black",
        ".",
    ],
    check=True,
)
