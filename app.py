# app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.param_functions import Query
from pytesseract import image_to_string
import requests
from io import BytesIO
from PIL import Image
from typing import List

app = FastAPI()

@app.post("/ocr")
async def ocr_image(files: List[UploadFile] = File(...)):
    """
    Endpoint: /ocr (POST)
    Description: Process multiple image files and extract text using OCR.
    Parameters:
        - files: List of image files to be uploaded.
    Returns:
        - A list of dictionaries containing the filename and the extracted text for each image.
    """
    results = []
    for file in files:
        image = Image.open(file.file)
        text = image_to_string(image)
        results.append({"filename": file.filename, "text": text})
    return results

@app.get("/ocr")
async def ocr_image_urls(urls: List[str] = Query(...)):
    """
    Endpoint: /ocr (GET)
    Description: Process multiple image URLs and extract text using OCR.
    Parameters:
        - urls: List of image URLs to be processed.
    Returns:
        - A list of dictionaries containing the URL and the extracted text for each image.
          If an error occurs while fetching an image, an error message is included instead of the text.
    """
    results = []
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            text = image_to_string(image)
            results.append({"url": url, "text": text})
        except requests.exceptions.RequestException as e:
            results.append({"url": url, "error": "Failed to fetch the image from the provided URL."})
    return results