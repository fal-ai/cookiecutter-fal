from .base import Field, FieldOptions

__prompt_input = FieldOptions(
    type="str",
    description=(
        "The prompt to use for generating the image. Be as descriptive as "
        "possible for best results."
    ),
    examples=[
        "an astronaut in the jungle, cold color palette with butterflies in the "
        "background, highly detailed, 8k"
    ],
)

Prompt = Field(
    title="Prompt",
    varname="prompt",
    input=__prompt_input,
    output=__prompt_input,
)


__negative_prompt_input = FieldOptions(
    type="str",
    description=(
        "The negative prompt to use. Use it to address details that you don't "
        "want in the image. This could be colors, objects, scenery and even the "
        "small details (e.g. moustache, blurry, low resolution)."
    ),
    examples=[
        (
            "cartoon, painting, illustration, worst quality, low quality, "
            "normal quality"
        ),
        "nsfw, cartoon, (epicnegative:0.9)",
    ],
    default="",
)

NegativePrompt = Field(
    title="Negative Prompt",
    varname="negative_prompt",
    input=__negative_prompt_input,
    output=__negative_prompt_input,
)

__image_size_input = FieldOptions(
    type="Optional[ImageSizeInput]",
    description=(
        "The size of the generated image. You can choose between some presets or "
        "custom height and width that **must be multiples of 8."
    ),
    default=repr("square_hd"),
)

ImageSize = Field(
    title="Image Size",
    varname="image_size",
    input=__image_size_input,
    output=__image_size_input,
)


__num_inference_steps_input = FieldOptions(
    type="int",
    description=(
        "The number of denoising steps. Increasing denoising steps usually "
        "improves image quality but makes the processing slower."
    ),
    default=30,
    ge=10,
    le=50,
)

InferenceSteps = Field(
    title="Number of Inference Steps",
    varname="num_inference_steps",
    input=__num_inference_steps_input,
    output=__num_inference_steps_input,
)

__guidance_scale_input = FieldOptions(
    type="int",
    description=(
        "The CFG (Classifier Free Guidance) scale is a measure of how close you "
        "want the model to stick to your prompt."
    ),
    default=7.5,
    ge=1.0,
    le=20.0,
)

GuidanceScale = Field(
    title="Classifier-Free Guidance scale (CFG)",
    varname="guidance_scale",
    input=__guidance_scale_input,
    output=__guidance_scale_input,
)

Seed = Field(
    title="Seed",
    varname="seed",
    input=FieldOptions(
        type="Optional[int]",
        default=None,
        examples=[3485908],
        description=(
            "The seed to use during the inference process. If `None` provided as seed "
            "value, a random seed will be used. Use it to get deterministic outputs."
        ),
    ),
    output=FieldOptions(
        type="int",
        examples=[3485908],
        description=("The seed used during the inference process."),
    ),
)

Image = Field(
    title="Image",
    varname="image",
    input=FieldOptions(
        description="The image to use for inference process.",
        type="Image",
        examples=[
            "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png'",
            "https://storage.googleapis.com/falserverless/illusion-examples/cubes.jpeg",
            "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        ],
    ),
    output=FieldOptions(
        description="The generated image.",
        type="Image",
        examples=[
            "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png'",
            "https://storage.googleapis.com/falserverless/illusion-examples/cubes.jpeg",
            "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        ],
    ),
)
