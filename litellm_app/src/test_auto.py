from openai import OpenAI
import os

def test_auto_model_proxy():
    """
    Tests the LiteLLM proxy with the 'auto' model feature using OpenAI API format.
    This should leverage LiteLLM's auto-routing to select an available model.
    """
    # Point the OpenAI client to the LiteLLM proxy
    client = OpenAI(
        base_url="http://localhost:4000",
        api_key="sk-not-needed" # API key is passed via LiteLLM's config/env
    )

    try:
        print("Sending request to LiteLLM proxy (OpenAI format) with 'auto' model...")
        chat_completion = client.chat.completions.create(
            model="auto",
            messages=[
                {
                    "role": "user",
                    "content": "こんにちは"
                }
            ]
        )

        print("\nResponse from LiteLLM proxy (using 'auto' model):")
        print(chat_completion.choices[0].message.content)
        print(f"Model used: {chat_completion.model}") # LiteLLM usually returns the model that was used

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure the LiteLLM proxy is running (docker compose up).")
        print("Ensure GEMINI_API_KEY, MISTRAL_API_KEY, and GROQ_API_KEY are set in your .env file.")
        print("Also ensure 'openai' python package is installed: pip install openai")

if __name__ == "__main__":
    test_auto_model_proxy()
