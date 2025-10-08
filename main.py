import os
from google import genai
from dotenv import load_dotenv


def main():
    load_dotenv()
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = "Explain what is the job of open ai?"
    response = client.models.generate_content(model="gemini-2.5-pro", contents=prompt)
    print(response.text)


main()
