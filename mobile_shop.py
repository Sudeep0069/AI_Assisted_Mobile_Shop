import os
import gradio as gr
from google import genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(),override=True)
api_key = os.getenv('GOOGLE_API_KEY')


client = genai.Client(api_key=api_key) if api_key else None

GEMINI_MODEL = "gemini-3.6-flash"

if __name__=='__main__':
    print(
        "Gemini configured."
        if client
        else "AI disabled; inventory features still work."
    )

mobiles = [
    {
        "id": 1,
        "brand": "Samsung",
        "model": "Galaxy S25",
        "price": 79999,
        "ram": "12GB",
        "storage": "256GB",
        "rating": 4.7,
        "stock": 10
    },
    {
        "id": 2,
        "brand": "Apple",
        "model": "iPhone 16",
        "price": 79900,
        "ram": "8GB",
        "storage": "128GB",
        "rating": 4.8,
        "stock": 8
    },
    {
        "id": 3,
        "brand": "OnePlus",
        "model": "OnePlus 13",
        "price": 69999,
        "ram": "12GB",
        "storage": "256GB",
        "rating": 4.6,
        "stock": 12
    },
    {
        "id": 4,
        "brand": "Google",
        "model": "Pixel 9",
        "price": 74999,
        "ram": "12GB",
        "storage": "256GB",
        "rating": 4.5,
        "stock": 7
    },
    {
        "id": 5,
        "brand": "Xiaomi",
        "model": "Xiaomi 15",
        "price": 59999,
        "ram": "12GB",
        "storage": "256GB",
        "rating": 4.4,
        "stock": 15
    },
    {
        "id": 6,
        "brand": "Realme",
        "model": "GT 7",
        "price": 42999,
        "ram": "12GB",
        "storage": "256GB",
        "rating": 4.3,
        "stock": 20
    }
]

