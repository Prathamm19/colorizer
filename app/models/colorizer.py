from deoldify.visualize import get_image_colorizer
from PIL import Image
import tempfile
import os
from pathlib import Path

# Define colorizer ONCE at the module level
colorizer = get_image_colorizer(artistic=True, root_folder=Path("C:/Users/prath/OneDrive/Desktop/Today/project_root"))


def colorize(pil_image):
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    temp_file.close()
    pil_image.save(temp_file.name)
    try:
        result_image = colorizer.get_transformed_image(
        temp_file.name,
        render_factor=35,
        watermarked=False
)
# No need to call Image.open if result is an image object

    finally:
        os.remove(temp_file.name)
    return result_image
