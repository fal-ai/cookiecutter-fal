from typing import Optional

from fal import function
from fal.toolkit import Image, ImageSizeInput, get_image_size
from pydantic import BaseModel, Field

from stable_diffusion.env import get_requirements, setup_environment
from stable_diffusion.model import get_pipeline


class StableDiffusionInput(BaseModel):
    prompt: str = Field(
        type=str,
        examples=[
            "an astronaut in the jungle, cold color palette with butterflies in the background, highly detailed, 8k"
        ],
        description="The prompt to use for generating the image. Be as descriptive as possible for best results.",
    )

    negative_prompt: str = Field(
        type=str,
        examples=[
            "cartoon, painting, illustration, worst quality, low quality, normal quality",
            "nsfw, cartoon, (epicnegative:0.9)",
        ],
        description="The negative prompt to use. Use it to address details that you don't want in the image. This could be colors, objects, scenery and even the small details (e.g. moustache, blurry, low resolution).",
        default="",
    )

    image_size: Optional[ImageSizeInput] = Field(
        type=Optional[ImageSizeInput],
        examples=None,
        description="The size of the generated image. You can choose between some presets or custom height and width that **must be multiples of 8.",
        default=None,
    )

    num_inference_steps: int = Field(
        type=int,
        examples=None,
        description="The number of denoising steps. Increasing denoising steps usually improves image quality but makes the processing slower.",
        ge=10,
        le=50,
        default=None,
    )

    guidance_scale: int = Field(
        type=int,
        examples=None,
        description="The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt.",
        ge=1.0,
        le=20.0,
        default=None,
    )

    seed: Optional[int] = Field(
        type=Optional[int],
        examples=[3485908],
        description="The seed to use during the inference process. If `None` provided as seed value, a random seed will be used. Use it to get deterministic outputs.",
    )

    image: Image = Field(
        type=Image,
        examples=[
            "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png'",
            "https://storage.googleapis.com/falserverless/illusion-examples/cubes.jpeg",
            "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        ],
        description="The image to use for inference process.",
    )


class StableDiffusionOutput(BaseModel):
    prompt: str = Field(
        type=str,
        examples=[
            "an astronaut in the jungle, cold color palette with butterflies in the background, highly detailed, 8k"
        ],
        description="The prompt to use for generating the image. Be as descriptive as possible for best results.",
    )

    negative_prompt: str = Field(
        type=str,
        examples=[
            "cartoon, painting, illustration, worst quality, low quality, normal quality",
            "nsfw, cartoon, (epicnegative:0.9)",
        ],
        description="The negative prompt to use. Use it to address details that you don't want in the image. This could be colors, objects, scenery and even the small details (e.g. moustache, blurry, low resolution).",
        default="",
    )

    image_size: Optional[ImageSizeInput] = Field(
        type=Optional[ImageSizeInput],
        examples=None,
        description="The size of the generated image. You can choose between some presets or custom height and width that **must be multiples of 8.",
        default=None,
    )

    num_inference_steps: int = Field(
        type=int,
        examples=None,
        description="The number of denoising steps. Increasing denoising steps usually improves image quality but makes the processing slower.",
        ge=10,
        le=50,
        default=None,
    )

    guidance_scale: int = Field(
        type=int,
        examples=None,
        description="The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt.",
        ge=1.0,
        le=20.0,
        default=None,
    )

    seed: int = Field(
        type=int,
        examples=[3485908],
        description="The seed used during the inference process.",
    )

    image: Image = Field(
        type=Image,
        examples=[
            "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png'",
            "https://storage.googleapis.com/falserverless/illusion-examples/cubes.jpeg",
            "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        ],
        description="The generated image.",
    )


@function(
    requirements=get_requirements(),
    machine_type="XS",
    keep_alive=60,
    serve=True,
    python_version="3.10",
)
def generate_image(input: StableDiffusionInput) -> StableDiffusionOutput:
    setup_environment()
    if input.image_size is not None:
        width = input.image_size.width
        height = input.image_size.height

    pipe = get_pipeline()

    # Generate images

    return StableDiffusionOutput()


if __name__ == "__main__":
    model_input = StableDiffusionInput()
    local = generate_image.on(serve=False)
    output = local(model_input)
    print(output)
