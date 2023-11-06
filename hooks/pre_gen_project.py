import sys
from collections import OrderedDict

available_fields = {{cookiecutter._fields}}

selected_input_fields = "{{ cookiecutter.input_fields }}"
selected_output_fields = "{{ cookiecutter.output_fields }}"

unexpected_input_fields = set(selected_input_fields.split()) - available_fields.keys()
unexpected_output_fields = set(selected_output_fields.split()) - available_fields.keys()

if unexpected_input_fields:
    print(f"Unexpected input fields: '{' '.join(unexpected_input_fields)}'")

if unexpected_output_fields:
    print(f"Unexpected output fields: '{' '.join(unexpected_output_fields)}'")

if unexpected_input_fields or unexpected_output_fields:
    sys.exit(-1)
