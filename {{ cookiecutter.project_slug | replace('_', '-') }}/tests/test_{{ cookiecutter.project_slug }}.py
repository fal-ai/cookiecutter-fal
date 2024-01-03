import json
from pathlib import Path
from tempfile import TemporaryDirectory

import httpx
import pytest
from fal import flags
from fal.sdk import get_default_credentials
from image_similarity_measures.evaluate import evaluation as image_similarity

{% set modal_name = cookiecutter.project_name | title | replace(' ', '') %}
{% set input_modal_name = modal_name + "Input" %}

from {{cookiecutter.project_slug}}.inference import (
    {{ cookiecutter.generate_function_name }},
    {{ input_modal_name }},
)

SIMILARITY_METHOD = "fsim"
SIMILARITY_THRESHOLD = 0.8

__CURR_DIR = Path(__file__).resolve().parent
__TEST_CASES_DIR = __CURR_DIR / "test_cases"


local_test_fn = {{ cookiecutter.generate_function_name }}.on(
    serve=False,
    keep_alive=600,
    _scheduler="nomad",
)

def get_test_cases():
    test_cases = []
    for test_case in __TEST_CASES_DIR.glob("*.json"):
        with open(test_case) as fp:
            test_case = json.load(fp)
            yield test_cases

@pytest.fixture(scope="session")
def rest_client() -> httpx.Client:
    credentials = get_default_credentials()
    with httpx.Client(
        base_url=flags.REST_URL, headers=credentials.to_headers()
    ) as client:
        yield client


@pytest.fixture(scope="session")
def image_client() -> httpx.Client:
    with httpx.Client() as client:
        yield client


def compare_images(
    client: httpx.Client, baseline_image: str, target_image: str
) -> float:
    with TemporaryDirectory() as directory:
        files = [f"{directory}/baseline.png", f"{directory}/target.png"]
        print("Comparing: ", baseline_image, target_image)
        for image_url, filename in zip([baseline_image, target_image], files):
            response = client.get(image_url)
            response.raise_for_status()
            with open(filename, "wb") as file:
                file.write(response.content)

        results = image_similarity(
            *files,
            metrics=[SIMILARITY_METHOD],
        )
        return results[SIMILARITY_METHOD]


@pytest.mark.parametrize(
    "name, input, output",
    [
        (
            test["name"],
            test["input"],
            test["output"],
        )
        for test in get_test_cases()
    ],
)
def test_{{ cookiecutter.project_slug }}(name, input, output, rest_client, image_client):
    model_input = {{ input_modal_name }}(**input)
    result = local_test_fn(model_input)

    for generated_image, expected_image in zip(result.images, output["images"]):
        response = rest_client.get(f"/storage/link/{expected_image}")
        response.raise_for_status()

        expected_image_url = response.json()["url"]
        similarity = compare_images(
            image_client,
            generated_image.url,
            expected_image_url,
        )
        assert similarity >= SIMILARITY_THRESHOLD
