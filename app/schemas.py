# Pydantic models for request/response, if using structured data
from pydantic import BaseModel

class ImageRequest(BaseModel):
    # Example for base64 or URL input
    image_data: str
