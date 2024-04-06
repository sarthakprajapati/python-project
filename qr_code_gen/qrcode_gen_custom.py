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
    watermark: Optional[str] = Field(None, example="/ptah/to/watermark.png")

@app.post("/generate")
async def generate_qr_code(url: Url):
    try:
        img = qrcode.make(url.url)
        img = img.convert("RGB")
        if url.watermark :
            # open the image 
            watermark = Image.open(url.watermark)
            # get the size of the qr code image 
            qr_height, qr_width = img.size
            # resize watermark to be smaller then the size of qr code 
            max_size = min(qr_width, qr_height) //5
            watermark = watermark.resize((max_size, max_size))
            # get size of resized watermark 
            watermark_height, watermark_width = watermark.size
            # calculate the position where to put the watermark 
            position = (qr_height-watermark_height)//2, (qr_width-watermark_width)//2
            # paste the watermark at the position 
            img.paste(watermark,position)


        filename = "qrcode-" + url.url.replace("/", "-").replace(":", "").replace(".", "-") + ".png"
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

