# Dockerfile

# Use Ubuntu 18.04 as base image
FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

# Update package list and install required software
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:alex-p/tesseract-ocr -y && \
    apt-get update -y && \
    apt-get install -y python3-dev libpython3.8-dev tesseract-ocr python3.8 python3-pip && \
    apt-get install -y libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev && \
    apt-get install -y libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk && \
    apt-get install -y libharfbuzz-dev libfribidi-dev libxcb1-dev && \
    apt-get install -y gcc g++ libfreetype6 libfreetype6-dev 

# Set up working directory
WORKDIR /app

# Copy requirements.txt into the working directory
COPY requirements.txt .

# Install Python packages from requirements.txt
RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

# Copy app.py into the working directory
COPY app.py .

# Expose the port for the FastAPI application
EXPOSE 8000

# Start the application using gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app", "-b", "0.0.0.0:8000"]
