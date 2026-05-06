import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()


def generate_text(prompt: str) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    model_name = os.getenv("MODEL_NAME")

    if not api_key:
      raise EnvironmentError("OPENROUTER_API_KEY environment variable is not set.")
    if not model_name:
      raise EnvironmentError("MODEL_NAME environment variable is not set.")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python main.py "<your prompt>"')
        sys.exit(1)

    user_prompt = " ".join(sys.argv[1:])
    result = generate_text(user_prompt)
    print(result)
