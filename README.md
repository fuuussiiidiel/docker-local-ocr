# ocr-api

Eine schlanke OCR-API auf Basis von [ocrmypdf](https://ocrmypdf.readthedocs.io/) und FastAPI.  
Ideal für lokale Verarbeitung ohne Cloud oder Drittanbieter.

## 🚀 Features

- PDF-Upload per HTTP POST
- OCR optional erzwingen (`force_ocr`)
- Antwort: fertige OCR-PDF-Datei als Download
- Komplett lokal ausführbar über Docker

## 🔧 Starten

```bash
docker-compose up --build
