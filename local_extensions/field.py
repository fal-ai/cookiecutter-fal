import json
from dataclasses import asdict
from typing import Any

from cookiecutter.utils import simple_filter

from .fields import FieldRegistry


@simple_filter
def load_fields(*args, **kwargs):
    fields = {}
    for name, field in FieldRegistry.items():
        fields[name] = field.to_dict()
    return json.dumps(fields)


@simple_filter
def todict(string, *args, **kwargs):
    return json.loads(string)


def _get_field_value(field: dict[str, Any]):
    example_field_value = None

    if field.get("examples"):
        example_field_value = field["examples"][0]

    elif field.get("default"):
        example_field_value = field["default"]

    return example_field_value


def _create_example_fields(fields: dict[str, Any], mode: str = "input"):
    example_fields = {}
    for field in fields.values():
        example_field_varname = field["varname"]
        example_field_value = _get_field_value(field[mode])
        example_fields[example_field_varname] = example_field_value
    return example_fields


@simple_filter
def create_example_test_case(fields):
    input_fields, output_fields = fields
    test_case = {"name": "Example test case"}

    test_case["input"] = _create_example_fields(input_fields, mode="input")
    test_case["output"] = _create_example_fields(output_fields, mode="output")

    return json.dumps(test_case, indent=4)
