import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import pathlib


def main():
    load_dotenv()
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    file_path = pathlib.Path("C:/Users/LENOVO/Downloads/1.pdf")
    prompt = "Summarize this document"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=file_path.read_bytes(),
                mime_type="application/pdf",
            ),
            prompt,
        ],
    )
    text = response.text
    createFile(text)


def createFile(text):
    with open("output.txt", "w") as file:
        file.write(text)


main()
