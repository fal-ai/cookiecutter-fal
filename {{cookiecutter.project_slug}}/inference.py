from {{ cookiecutter.project_slug }}.env import get_requirements
from {{ cookiecutter.project_slug }}.model import get_pipeline

from fal import function
from pydantic import BaseModel, Field

{% if 'image_size' in cookiecutter.input_fields.split(' ') or 'image_size' in cookiecutter.output_fields.split(' ') 
    or 'seed' in cookiecutter.input_fields.split(' ') or 'seed' in cookiecutter.output_fields.split(' ') 
%}
from typing import Optional
{% endif %}

{% if 'image' in cookiecutter.input_fields.split(' ') or 'image' in cookiecutter.output_fields.split(' ') %}
from fal.toolkit import Image
{% endif %}

class {{ cookiecutter.project_name | title | replace(' ', '') }}Input(BaseModel):
{%- if cookiecutter.input_fields|trim|length == 0 %}
    pass
{%- else %}
{%- for field in cookiecutter.input_fields.split(' ') %}
    {% if field in cookiecutter._fields -%}
        {{ field }}: {{ cookiecutter._fields[field].type }} = Field(
        {% for arg in cookiecutter._fields[field].args -%}
            {{ arg }}={{cookiecutter._fields[field].args[arg]}},
        {% endfor %}
    )
    {%- endif -%}
{% endfor %}
{% endif %}

class {{ cookiecutter.project_name | title | replace(' ', '') }}Output(BaseModel):
{%- if cookiecutter.output_fields|trim|length == 0 %}
    pass
{%- else %}
{%- for field in cookiecutter.output_fields.split(' ') %}
    {% if field in cookiecutter._fields -%}
        {{ field }}: {{ cookiecutter._fields[field].type }} = Field(
        {{ "description" }}={{cookiecutter._fields[field].args["description"]}},
    )
    {%- endif -%}
{% endfor %}
{%- endif %}



@function(
    requirements=get_requirements(),
    machine_type="{{ cookiecutter.machine_type }}",
    keep_alive={{ cookiecutter.keep_alive }},
    serve=True,
    python_version="3.10",
)
def {{ cookiecutter.generate_function_name }}(input: {{ cookiecutter.project_name | title | replace(' ', '') }}Input) -> {{ cookiecutter.project_name | title | replace(' ', '') }}Output:
{%- if 'image_size' in cookiecutter.input_fields.split(' ') %}
    if input.image_size is not None:
        width = input.image_size.width
        height = input.image_size.height
{% endif %}

    pipe = get_pipeline()

    # Generate images

    return {{ cookiecutter.project_name | title | replace(' ', '') }}Output()




if __name__ == "__main__":
    model_input = {{ cookiecutter.project_name | title | replace(' ', '') }}Input(
    {%- for field in cookiecutter.input_fields.split(' ') %}
        {% if field in cookiecutter._fields -%}
            {{ field }}={{ cookiecutter._fields[field].args["default"] }},
        {%- endif -%}
        {% endfor %}
    )
    local = {{ cookiecutter.generate_function_name }}.on(serve=False)
    output = local(model_input)
    print(output)
