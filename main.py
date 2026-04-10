from schemas.response import ResponseModel
from service.predict import predict_ai
from fastapi import FastAPI, File, HTTPException, UploadFile

api = FastAPI()



@api.get('/')
def home():
    return {"status": "API running"}

@api.post('/predict',response_model=ResponseModel)
async def predict(image: UploadFile = File(...)):
    
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    image_bytes = await image.read()

    result = predict_ai(image_bytes, image.content_type)

    return result