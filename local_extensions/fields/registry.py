from .prompt import *
from .base import Field

__snapshot = globals().copy()

FieldRegistry: dict[str, Field] = {}

for key, value in __snapshot.items():
    if isinstance(value, Field):
        FieldRegistry[value.title] = value
