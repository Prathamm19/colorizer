from PIL import Image
import tempfile
import os
import subprocess
import sys
from pathlib import Path

# Clone DeOldify if not already present
if not os.path.exists('DeOldify'):
    subprocess.run(['git', 'clone', 'https://github.com/jantic/DeOldify.git'])

# Add DeOldify to system path
sys.path.append(str(Path("DeOldify").resolve()))

# Create required dummy directory to prevent fastai crash
dummy_path = Path("DeOldify/dummy/test")
dummy_path.mkdir(parents=True, exist_ok=True)

# Import colorizer
from DeOldify.deoldify.visualize import get_image_colorizer

# ✅ USE RELATIVE PATH — important for cloud deployments!
colorizer = get_image_colorizer(artistic=True, root_folder=Path("DeOldify"))

def colorize(pil_image: Image.Image) -> Image.Image:
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    temp_file.close()
    pil_image.save(temp_file.name)
    try:
        result_image = colorizer.get_transformed_image(
            temp_file.name,
            render_factor=35,
            watermarked=False
        )
        return result_image  # Already a PIL Image
    finally:
        os.remove(temp_file.name)
