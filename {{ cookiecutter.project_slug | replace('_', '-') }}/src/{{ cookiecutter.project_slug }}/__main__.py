import fal

from {{ cookiecutter.project_slug }}.inference import {{ cookiecutter.app_class_name }}

app = fal.wrap_app({{ cookiecutter.app_class_name }})
app()
