# AI-Powered Interview

This project provides a simple interface for running a mock interview. The user will speak and the interviewer will also respond. The entire conversation is transcribed so the system can analyze it and generate feedback.

## Using Gemini for Responses

To experiment with Gemini's free AI credits, a small example script is provided in `src/gemini_example.py`.

### Setup

1. Create a Python virtual environment and install the required library:

```bash
pip install google-generativeai
```

2. Obtain an API key for the Gemini API and export it as an environment variable:

```bash
export GEMINI_API_KEY=<YOUR_API_KEY>
```

### Run the Example

Execute the script with:

```bash
python src/gemini_example.py
```

Then enter a prompt when asked. The script sends the prompt to the Gemini API and prints the AI's response.

