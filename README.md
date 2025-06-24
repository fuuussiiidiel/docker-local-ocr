# ocr-api

Eine schlanke OCR-API auf Basis von [ocrmypdf](https://ocrmypdf.readthedocs.io/) und FastAPI.  
Ideal für lokale Verarbeitung ohne Cloud oder Drittanbieter.

## 🚀 Features

- PDF-Upload per HTTP POST
- OCR optional erzwingen (`force_ocr`)
- Antwort: fertige OCR-PDF-Datei als Download
- Komplett lokal ausführbar über Docker
- Einfach integrierbar in Tools wie **n8n**

## 🔧 Starten

```bash
docker-compose up --build```

Die API ist danach erreichbar unter:
http://localhost:8089/ocr

## 📤 Beispiel-Request (mit curl)
```bash
curl -F "file=@scan.pdf" -F "force_ocr=true" http://localhost:8089/ocr --output result.pdf```

## 🔁 Nutzung mit n8n
In einem HTTP Request Node in n8n:

Methode: POST
URL: http://localhost:8089/ocr
Body Content Type: multipart/form-data
Form Fields:
file → Binärdatei (PDF)
force_ocr → true oder false (optional)

Antwort:
Die verarbeitete PDF-Datei kommt direkt im HTTP-Response zurück und kann in n8n weiterverwendet werden.
