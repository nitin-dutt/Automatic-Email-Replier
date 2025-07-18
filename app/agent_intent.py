import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key= GEMINI_API_KEY)
model= genai.GenerativeModel("gemini-2.0-flash")

def classify_intent(text):
    prompt=f"""
    You are an email intent classifier.
    Given the email below, classify it as one of: Query, Complaint, Meeting Request,Spam,Other.
    
    EMAIL:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
    