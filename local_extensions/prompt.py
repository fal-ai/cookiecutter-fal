import json

import inquirer
from cookiecutter.utils import simple_filter


@simple_filter
def select_multiple_field(options: str):
    choices = json.loads(options)
    choice = inquirer.checkbox(
        message=(
            "Select which fields you want to use (Use Arrow keys to Select/Deselect "
            "and Enter key to confirm selections)"
        ),
        choices=choices,
    )
    selected_options = {choice: choices[choice] for choice in choice}
    return json.dumps(selected_options)


@simple_filter
def select_multiple(options: str):
    choices = json.loads(options)
    choice = inquirer.checkbox(
        message=(
            "Select which fields you want to use (Use Arrow keys to Select/Deselect "
            "and Enter key to confirm selections)"
        ),
        choices=choices,
    )
    return choice


@simple_filter
def select_one(options: list):
    choice = inquirer.list_input(
        message="Select which field you want to use",
        choices=options,
        default=options[0],
    )
    return choice
