import os
from google.generativeai import configure, GenerativeModel

def generate_text(prompt: str) -> str:
    """Generate a completion using Gemini API."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set the GEMINI_API_KEY environment variable.")

    configure(api_key=api_key)
    model = GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


def main() -> None:
    prompt = input("Enter a prompt: ")
    result = generate_text(prompt)
    print(result)


if __name__ == "__main__":
    main()
