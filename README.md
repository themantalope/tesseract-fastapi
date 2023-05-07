# tesseract-ocr and fastapi

little project to set up a tesseract-ocr server with fastapi

## endpoints

### POST

- **Description**: Process multiple image files and extract text using OCR.
- **Parameters**:
  - `files` (form-data): List of image files to be uploaded.
- **Returns**:
  - A list of dictionaries containing the filename and the extracted text for each image.

### GET

- **Description**: Process multiple image URLs and extract text using OCR.
- **Parameters**:
  - `urls` (query): List of image URLs to be processed.
- **Returns**:
  - A list of dictionaries containing the URL and the extracted text for each image. If an error occurs while fetching an image, an error message is included instead of the text.

## Usage

1. Build the Docker image: `docker build -t ocr-app .`
2. Run the Docker container: `docker run -p 8000:8000 ocr-app`
3. Access the OCR API at `http://localhost:8000/ocr`.
