from openai import OpenAI
import os

def test_gemini_proxy_openai_format():
    """
    Tests the LiteLLM proxy with the Gemini model using OpenAI API format.
    """
    # Point the OpenAI client to the LiteLLM proxy
    client = OpenAI(
        base_url="http://localhost:4000",
        api_key="sk-not-needed" # API key is passed via LiteLLM's config/env
    )

    try:
        print("Sending request to LiteLLM proxy (OpenAI format) with Gemini model...")
        chat_completion = client.chat.completions.create(
            model="gemini-3-flash",
            messages=[
                {
                    "role": "user",
                    "content": "こんにちは"
                }
            ]
        )

        print("\nResponse from LiteLLM proxy:")
        print(chat_completion.choices[0].message.content)

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure the LiteLLM proxy is running (docker compose up).")
        print("Your GEMINI_API_KEY should be set in the .env file.")
        print("Also ensure 'openai' python package is installed: pip install openai")

if __name__ == "__main__":
    test_gemini_proxy_openai_format()