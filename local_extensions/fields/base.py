from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class FieldOptions:
    type: T
    description: str
    examples: list[T] | None = None
    default: T | None = None
    ge: T | None = None
    gt: T | None = None
    lt: T | None = None
    le: T | None = None

    def get_default(self) -> T | None:
        if self.type == "str":
            return repr(self.default)
        return self.default

    def to_dict(self) -> dict[str, Any]:
        field_dict = {
            "type": self.type,
            "description": repr(self.description),
        }

        extras = ["examples", "ge", "gt", "lt", "le"]
        for extra in extras:
            if getattr(self, extra) is not None:
                field_dict[extra] = getattr(self, extra)

        if (
            self.default is None and "Optional" in self.type
        ) or self.default is not None:
            field_dict["default"] = self.get_default()

        return field_dict


@dataclass
class Field:
    title: str
    varname: str
    input: FieldOptions | None = None
    output: FieldOptions | None = None

    def to_dict(self) -> dict[str, Any]:
        field_dict = {
            "title": self.title,
            "varname": self.varname,
        }

        if self.input is not None:
            field_dict["input"] = self.input.to_dict()

        if self.output is not None:
            field_dict["output"] = self.output.to_dict()

        return field_dict
