import re

from google import genai
from google.genai import types
# from dotenv import load_dotenv
import os
import json

# load_dotenv()

# ✅ fix
api_key = os.getenv("Gemini_API_Key")
print(f"API KEY LOADED: {api_key[:5] if api_key else 'NOT FOUND'}")
client = genai.Client(api_key=api_key)

def predict_ai(image_bytes: bytes, mime_type: str):
    prompt = """
    You are a plant disease expert.
    Analyze this plant image and return ONLY a JSON object like this:
    {
        "disease": "disease name",
        "description": "what is this disease",
        "treatment": ["step 1", "step 2", "step 3"],
        "severity": "low or medium or high",
        "healthy": false
    }
    If the plant is healthy return:
    {
        "healthy": true,
        "disease": null,
        "description": "Plant looks healthy",
        "treatment": [],
        "severity": null
    }
    If the image is NOT a plant return:
    {
        "error": "not a plant"
    }
    Return ONLY the JSON. No extra text.
    """

    #send image in new library
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type 
            ),
            prompt
        ]
    )
        # Strip markdown code fences
    
    raw = response.text.strip()
    print("RAW BEFORE STRIP:", repr(raw))  # 👈 shows exact characters

    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    raw = raw.strip()

    print("RAW AFTER STRIP:", repr(raw))  # 👈 confirm it's clean


    try:
        result = json.loads(raw)
        return result
    except json.JSONDecodeError as e:
        print("JSON PARSE ERROR:", e)
        print("RAW TEXT WAS:", response.text)
        return {"error": "Invalid AI response", "raw": response.text}
   