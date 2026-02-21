#!/bin/bash

# Test the LiteLLM proxy with the Gemini model

echo "Testing LiteLLM proxy with Gemini model..."

curl -X POST http://localhost:4000/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "gemini-3-flash",
  "messages": [
    {
      "role": "user",
      "content": "あなたはだれですか？"
    }
  ]
}'

echo ""
echo "Please ensure the LiteLLM proxy is running (docker compose up)."
echo "You also need to set your GEMINI_API_KEY in the .env file."
