# Imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from PIL import Image
import os
import qrcode


app = FastAPI()

class Url(BaseModel):
    url: str = Field(..., example="https://example.com")

@app.post("/generate")
async def generate_qr_code(url: Url):
    try:
        img = qrcode.make(url.url)
        filename = "qrcode.png"
        img.save(os.path.dirname(os.path.realpath(__file__)) + "/qrcodes/" +  filename)
        return {"message": "QR code generated successfully!!", "qrcode": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# python -m uvicorn main:app --reload
# http://127.0.0.1:8000/docs#/
# http://localhost:8000/redoc

