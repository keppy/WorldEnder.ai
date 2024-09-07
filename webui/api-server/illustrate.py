import os
import asyncio
import requests
import logging
from worldender.models.illustration import Illustration
from worldender.config import app_config
from typing import Callable
from .storage import store_illustration_error, store_illustration_filepath

logger = logging.getLogger(__name__)


def send_generation_request(
    host,
    params,
):
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {app_config.stabilityai_api_key}",
    }

    # Encode parameters
    files = {}
    image = params.pop("image", None)
    mask = params.pop("mask", None)
    if image is not None and image != "":
        files["image"] = open(image, "rb")
    if mask is not None and mask != "":
        files["mask"] = open(mask, "rb")
    if len(files) == 0:
        files["none"] = ""

    # Send request
    print(f"Sending REST request to {host}...")
    response = requests.post(host, headers=headers, files=files, data=params)
    if not response.ok:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

    return response


def gen_illustrate(
    id: str,
    prompt: str,
    negative_prompt="",
    aspect_ratio="1:1",
    output_format="png",
) -> Illustration:
    """
    someone else has created and stored the illustration. This
    code asynchronously requests the actual image from stability
    once the image is ready, store the pixels in a path on the file system
    and update the illustration object in the database with the path
    and new state
    """
    try:
        seed = 0  # @param {type:"integer"}
        model = (
            "sd3-large-turbo"  # @param ["sd3-large", "sd3-large-turbo", "sd3-medium"]
        )

        host = f"https://api.stability.ai/v2beta/stable-image/generate/sd3"

        params = {
            "prompt": prompt,
            "negative_prompt": negative_prompt if model == "sd3" else "",
            "aspect_ratio": aspect_ratio,
            "seed": seed,
            "output_format": output_format,
            "model": model,
            "mode": "text-to-image",
        }
        response = send_generation_request(host, params)

        # Decode response
        output_image = response.content
        finish_reason = response.headers.get("finish-reason")
        seed = response.headers.get("seed")

        # Check for NSFW classification
        if finish_reason == "CONTENT_FILTERED":
            raise Warning("Generation failed NSFW classifier")

        # Save and display result
        file_name = os.path.join(
            app_config.illustration_path, f"generated_{seed}.{output_format}"
        )
        with open(file_name, "wb") as f:
            f.write(output_image)
        logger.info(f"Saved image {file_name}")

        # Update illustration object
        # asyncio.run(store_illustration_filepath(id, file_name))
        store_illustration_filepath(id, file_name)
        # loop.run_until_complete(on_complete(id, file_name))
    except Exception as e:
        store_illustration_error(id)
        raise e
