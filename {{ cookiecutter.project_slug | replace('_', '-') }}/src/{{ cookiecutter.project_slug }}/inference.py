{% set input_model_name = cookiecutter.app_class_name + "Input" %}
{% set output_model_name = cookiecutter.app_class_name + "Output" %}

from {{ cookiecutter.project_slug }}.env import get_requirements, setup_environment
from {{ cookiecutter.project_slug }}.models import {{ input_model_name }}, {{ output_model_name }}
from {{ cookiecutter.project_slug }}.pipeline import get_pipeline

import fal


class {{ cookiecutter.app_class_name }}(
    fal.App,
    keep_alive={{ cookiecutter.keep_alive }},
):  # type: ignore
    requirements=get_requirements()
    machine_type="{{ cookiecutter.machine_type }}"

    def setup(self):
        setup_environment()
        self.pipeline = get_pipeline()

    @fal.endpoint("/")
    def {{ cookiecutter.generate_function_name }}(self, input: {{ input_model_name }}) -> {{ output_model_name }}:
        return {{ output_model_name }}()

