from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import ocrmypdf
import uuid, shutil, os

app = FastAPI()

@app.post("/ocr")
async def ocr_pdf(file: UploadFile = File(...), force_ocr: bool = Form(False)):
    in_path = f"/tmp/{uuid.uuid4()}.pdf"
    out_path = f"/tmp/ocr_{uuid.uuid4()}.pdf"

    with open(in_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        ocrmypdf.ocr(
            in_path,
            out_path,
            force_ocr=force_ocr,
            output_type="pdf"
        )
    except Exception as e:
        return {"error": str(e)}

    return FileResponse(out_path, media_type="application/pdf")
