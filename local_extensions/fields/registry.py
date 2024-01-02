from .base import Field
from .prompt import *

__snapshot = globals().copy()

FieldRegistry: dict[str, Field] = {}

for key, value in __snapshot.items():
    if isinstance(value, Field):
        FieldRegistry[value.title] = value
