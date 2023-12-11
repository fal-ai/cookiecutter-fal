from dataclasses import asdict
from .fields import FieldRegistry
from cookiecutter.utils import simple_filter
import json


@simple_filter
def load_fields(*args, **kwargs):
    fields = {}
    for name, field in FieldRegistry.items():
        fields[name] = field.to_dict()
    return json.dumps(fields)


@simple_filter
def todict(string, *args, **kwargs):
    return json.loads(string)
