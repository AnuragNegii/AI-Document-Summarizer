
import os
from google import  genai

def main():
    GEMINI_API_KEY = os.envroment.get
    client = genai.Client(api_key=GEMINI_API_KEY)

    print(client)
    print("Hello world")

main()
