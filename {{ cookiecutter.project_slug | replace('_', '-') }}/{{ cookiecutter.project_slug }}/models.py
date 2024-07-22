from pydantic import BaseModel

{% set input_model_name = cookiecutter.app_class_name + "Input" %}
{% set output_model_name = cookiecutter.app_class_name + "Output" %}


class {{ input_model_name }}(BaseModel):
    pass

class {{ output_model_name }}(BaseModel):
    pass

