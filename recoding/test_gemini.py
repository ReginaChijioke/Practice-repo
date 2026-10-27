
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key missing.")
else:
    try:
        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                timeout=120000,
                retry_options=types.HttpRetryOptions(attempts=1),
            ),
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents="Reply with the single word OK.",
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                ),
                max_output_tokens=64,
            ),
        )

        print("Gemini response:", response.text)

        print("Gemini response:", response.text)

    except Exception as error:
        print("Gemini test failed:", type(error).__name__)
        print(error)
