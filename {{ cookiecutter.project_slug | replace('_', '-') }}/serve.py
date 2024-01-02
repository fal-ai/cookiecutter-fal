import configparser
import subprocess
from pathlib import Path

__FILE_DIR = Path(__file__).resolve().parent
# We assume that the config file is in the same directory as this script.
FAL_CONFIG_PATH = __FILE_DIR / "fal.ini"


def is_subsection(section: str):
    return section.startswith("[") and section.endswith("]")


def get_subsection_name(section: str):
    return section[1:-1]


def validate_subsection(config: configparser.ConfigParser, section: str):
    if not is_subsection(section):
        raise ValueError(
            f"Section {section} is not a subsection. Subsections must be "
            "enclosed in square brackets."
        )

    if not get_subsection_name(section):
        raise ValueError(
            f"Section {section} is an empty subsection. Subsections must have "
            "a name."
        )

    subsection_config = dict(config.items(section))
    validate_subsection_config(section, subsection_config)


def validate_section(config: configparser.ConfigParser, section: str):
    if is_subsection(section):
        raise ValueError(
            f"Section {section} is a subsection. Subsections must be defined "
            "after a section."
        )

    if len(config.items(section)) != 0:
        raise ValueError(
            f"Section {section} is not empty. Sections should only contain "
            "subsections."
        )


def validate_subsection_config(subsection: str, subsection_config: dict[str, str]):
    required_keys = ["alias", "auth"]
    missing_keys = []
    additional_keys = []

    for key in required_keys:
        if key not in subsection_config:
            missing_keys.append(key)

    for key in subsection_config:
        if key not in required_keys:
            additional_keys.append(key)

    if missing_keys:
        raise ValueError(
            f"Missing required keys in subsection [{subsection}]: {missing_keys}"
        )

    if additional_keys:
        raise ValueError(
            f"Additional keys in subsection [{subsection}]: {additional_keys}"
        )


def parse_subsection(config: configparser.ConfigParser, section: str):
    validate_subsection(config, section)

    subsection_config = dict(config.items(section))
    return subsection_config


def parse_sections_from_config(config: configparser.ConfigParser):
    parsed_sections = {}  # type: ignore
    current_section = None

    for section in config.sections():
        if is_subsection(section):
            if not current_section:
                raise ValueError(
                    f"Subsection [{section}] found before a section was defined "
                    "in the config file. Please define a section before "
                    "defining a subsection."
                )

            subsection_name = get_subsection_name(section)
            subsection_config = parse_subsection(config, section)
            parsed_sections[current_section][subsection_name] = subsection_config
        else:
            validate_section(config, section)
            current_section = section
            parsed_sections[current_section] = {}

    return parsed_sections


def get_sections() -> dict[str, dict[str, dict[str, str]]]:
    with open(FAL_CONFIG_PATH) as fp:
        config = configparser.ConfigParser()
        config.read_file(fp)

    sections = parse_sections_from_config(config)

    return sections


# TODO: If its already deployed, we should downscale and lower the keep alive before
# deploying again.
def serve_fal_function(
    module_name: str, function_name: str, alias: str, auth: str, dry_run: bool = True
):
    file_path = module_name.replace(".", "/") + ".py"
    command = [
        "fal",
        "fn",
        "serve",
        file_path,
        function_name,
        "--alias",
        alias,
        "--auth",
        auth,
    ]

    print("Deploying to fal with:", " ".join(command))
    if not dry_run:
        subprocess.run(command, check=True)


if __name__ == "__main__":
    sections = get_sections()
    for module_name, function_names in sections.items():
        for function_name, function_config in function_names.items():
            serve_fal_function(
                module_name=module_name,
                function_name=function_name,
                alias=function_config["alias"],
                auth=function_config["auth"],
            )
