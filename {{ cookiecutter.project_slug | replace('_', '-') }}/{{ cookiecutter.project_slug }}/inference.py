from {{ cookiecutter.project_slug }}.env import get_requirements, setup_environment
from {{ cookiecutter.project_slug }}.model import get_pipeline

import fal
from pydantic import BaseModel, Field

{% set input_fields = cookiecutter.__input_fields | todict %}
{% set output_fields = cookiecutter.__output_fields | todict %}
{% set modal_name = cookiecutter.project_name | title | replace(' ', '') %}


{% if 'Image Size' in input_fields or 'Image Size' in output_fields
    or 'seed' in input_fields or 'seed' in output_fields
%}
from typing import Optional
{% endif %}

{% if 'Image' in input_fields or 'Image' in output_fields %}
from fal.toolkit import Image, ImageSizeInput, get_image_size
{% endif %}

class {{ modal_name }}Input(BaseModel):
{%- if not input_fields %}
    pass
{%- else %}
{%- for field in input_fields -%}
    {% set field_value = input_fields[field] %}
    {{ field_value.varname }}: {{ field_value.input.type }} = Field(
    {% for arg in field_value.input -%}
        {{ arg }}={{field_value.input[arg]}},
    {% endfor %}
    )
{%- endfor %}
{% endif %}

class {{ modal_name }}Output(BaseModel):
{%- if not output_fields %}
    pass
{%- else %}
{%- for field in output_fields -%}
    {% set field_value = output_fields[field] %}
    {{ field_value.varname }}: {{ field_value.output.type }} = Field(
    {% for arg in field_value.output -%}
        {{ arg }}={{field_value.output[arg]}},
    {% endfor %}
    )
{%- endfor %}
{%- endif %}



@fal.function(
    requirements=get_requirements(),
    machine_type="{{ cookiecutter.__machine_type }}",
    keep_alive={{ cookiecutter.keep_alive }},
    serve=True,
    python_version="3.10",
)
def {{ cookiecutter.generate_function_name }}(input: {{ modal_name }}Input) -> {{ modal_name }}Output:
{%- if 'Image Size' in input_fields %}
    if input.image_size is not None:
        image_size = get_image_size(input.image_size)
        width = input.image_size.width
        height = input.image_size.height
{% endif %}

    setup_environment()



    pipe = get_pipeline()

    # Generate images

    return {{ modal_name }}Output()




if __name__ == "__main__":
    model_input = {{ modal_name }}Input(
    {%- for field in input_fields %}
    {% endfor %}
    )
    local = {{ cookiecutter.generate_function_name }}.on(serve=False)
    output = local(model_input)
    print(output)
