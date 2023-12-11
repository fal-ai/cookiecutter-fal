"""
This module handles environment setup and configuration for the project. It contains
functions and variables related to setting up the project environment, such as managing
dependencies, external repositories, or configuring environment variables.
Additionally, it may include constants or configuration parameters used throughout the
project.

Contents:
- Functions for managing environment setup.
- Configuration parameters and constants.
- Any necessary dependencies or packages to be installed.
"""

from pathlib import Path

__CURR_DIR = Path(__file__).resolve().parent


def get_requirements():
    with open(__CURR_DIR / "requirements.txt") as fp:
        requirements = fp.read().split()
    return requirements


def download_models():
    pass


def setup_environment():
    download_models()
