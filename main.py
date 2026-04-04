from service.predict import predict_ai
from fastapi import FastAPI, File, HTTPException, UploadFile
import base64

api = FastAPI()

#cruds API 
@api.get('/')
def home():
    return {"status": "API running"}

@api.post('/predict')
async def predict(image: UploadFile = File(...)):
    #read image by bits
    image_bits = await image.read()

    #encode image to base64
    image_base64 = base64.b64encode(image_bits).decode('utf-8')

    return {"filename": image.filename, "message": "image received successfully", "image": image_base64[:50] }
