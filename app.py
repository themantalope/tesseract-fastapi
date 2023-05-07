# app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.param_functions import Query
from pytesseract import image_to_string
import requests
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    image = Image.open(file.file)
    text = image_to_string(image)
    return {"text": text}

@app.get("/ocr")
async def ocr_image_url(url: str = Query(...)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        text = image_to_string(image)
        return {"text": text}
    except requests.exceptions.RequestException as e:
        return JSONResponse(content={"error": "Failed to fetch the image from the provided URL."}, status_code=400)
