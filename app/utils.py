# Helper functions for image processing
from PIL import Image
import io

def read_image_from_bytes(image_bytes):
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")

def save_image_to_bytes(pil_image, format="JPEG"):
    buf = io.BytesIO()
    pil_image.save(buf, format=format)
    buf.seek(0)
    return buf
