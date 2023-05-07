# tesseract-ocr and fastapi

little project to set up a tesseract-ocr server with fastapi

## enpoints

### /ocr

- method: POST

  - body: multipart/form-data
    - image: file

- method: GET
  - params:
    - url: str
