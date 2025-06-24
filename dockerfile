FROM python:3.11-slim

# Abhängigkeiten für ocrmypdf
RUN apt-get update && apt-get install -y \
    ghostscript \
    tesseract-ocr \
    qpdf \
    unpaper \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libopenjp2-7 \
    && rm -rf /var/lib/apt/lists/*

# ocrmypdf installieren
RUN pip install ocrmypdf fastapi uvicorn python-multipart

# Arbeitsverzeichnis und Code
WORKDIR /app
COPY app.py .

# HTTP-Server starten
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8089"]
