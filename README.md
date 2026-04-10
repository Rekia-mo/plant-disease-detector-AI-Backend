# 🌿 Plant Disease ai Detector

## 📋 Description
An AI-powered web application that detects plant diseases from photos.
Upload a photo of your plant and get a diagnosis in under 10 seconds.
The app also detects if the plant is healthy or if the uploaded image is not a plant at all.

## ✨ What it returns
```json
{
  "disease": "disease name",
  "description": "what is this disease",
  "treatment": ["step 1", "step 2", "step 3"],
  "severity": "low | medium | high",
  "healthy": false
}
```
If the plant is healthy return:
```json
{
  "healthy": true,
  "disease": null,
  "description": "Plant looks healthy",
  "treatment": [],
  "severity": null
}
```
If the image is NOT a plant return:
```
{
  "error": "not a plant"
}
```

## 🛠️ Tech Stack
- Python
- FastAPI
- Google Gemini API (gemini-2.0-flash-lite)

## 🚀 How to run locally
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file and add your Gemini API key
5. Run: `uvicorn main:api --reload`

## 📡 API Endpoint
`POST /predict`
- Body: `form-data`
- Key: `image` (type: File)

## 🔑 Environment Variables
Gemini_API_Key=your_key_here

## 🌍 Live Demo
Backend: https://plant-disease-detector-ai-backend-production.up.railway.app

Frontend: coming soon 🚧
