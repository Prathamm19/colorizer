from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from app.models.colorizer import colorize
import io
from PIL import Image

app = FastAPI()

@app.post("/colorize")
async def colorize_image(image: UploadFile = File(...)):
    img_bytes = await image.read()
    input_image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    output_image = colorize(input_image)
    buf = io.BytesIO()
    output_image.save(buf, format="JPEG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/jpeg")
