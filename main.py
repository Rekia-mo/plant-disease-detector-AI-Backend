from fastapi import FastAPI

api = FastAPI()

#cruds API 
@api.get('/')
def home():
    return {"message": "Hello Worldii"}