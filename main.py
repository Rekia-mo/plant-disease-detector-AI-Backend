from schemas.response import ResponseModel
from service.predict import predict_ai
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # must be False when using ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

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