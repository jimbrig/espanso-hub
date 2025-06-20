#!/usr/bin/env python

"""
ask-ai.py: Query a local or remote LLM (Large Language Model) using the OpenAI API interface and return the response.

Author: Bernhard Enders
Date: 2025-06-14
Version: 0.1.0

Description:
    This script is designed for integration with Espanso, allowing users to send a prompt to an LLM and receive a direct answer, suitable for text expansion workflows.

Features:
    - Loads configuration (API key, base URL, model) from a .env file in the script directory.
    - Sends the user-provided prompt to the LLM with a system message enforcing non-interactive, assumption-based responses.
    - Prints the LLM's response to stdout for Espanso to capture.
    - Handles errors gracefully and provides clear error messages if configuration or API calls fail.

Usage:
    python ask-ai.py "<text>"

Requirements:
    - openai
    - python-dotenv
    - Python 3.9+
"""

import os
import shutil
import sys
sys.stdout.reconfigure(encoding="utf-8")

# packages dependency check
REQUIRED_PACKAGES = ["openai", "dotenv"]
missing = []
for pkg in REQUIRED_PACKAGES:
    try:
        __import__(pkg)
    except ImportError:
        missing.append(pkg)
if missing:
    print(f"❌ Error: Missing required packages: {', '.join(missing)}. Please install them with 'pip install -r requirements.txt'.")
    sys.exit(0)

from openai import OpenAI
from dotenv import load_dotenv


def ensure_env_file() -> None:
    """
    Ensures that a .env file exists. If not, tries to copy example.env to .env using shutil.copy.
    Raises FileNotFoundError if neither exists, lets OSError propagate on copy failure.
    """
    script_dir = os.path.dirname(__file__)
    env_path = os.path.join(script_dir, ".env")
    example_env_path = os.path.join(script_dir, "example.env")

    if not os.path.exists(env_path):
        if os.path.exists(example_env_path):
            shutil.copy(example_env_path, env_path)
        else:
            raise FileNotFoundError(f"❌ Error: Missing .env file in directory: '{script_dir}'.")

def load_and_validate_env() -> tuple[str, str, str]:
    """
    Loads and validates .env configuration. Returns (api_key, base_url, model).
    Raises ValueError if any required variable is missing.
    """
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = os.getenv("MODEL")
    if not api_key:
        raise ValueError("❌ Error: API_KEY variable not found in .env file!")
    if not base_url:
        raise ValueError("❌ Error: BASE_URL variable not found in .env file!")
    if not model:
        raise ValueError("❌ Error: MODEL variable not found in .env file!")
    return api_key, base_url, model

def ask_ai(text: str) -> str:
    """
    Sends a prompt to a local or remote LLM using the OpenAI API interface and returns the response.

    Args:
        text (str): The user prompt to send to the LLM.

    Returns:
        str: The LLM's response or an error message.
    """
    try:
        ensure_env_file()
        api_key, base_url, model = load_and_validate_env()
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are operating in a non-interactive mode.\n"
                        "Do NOT use introductory phrases, greetings, or opening messages.\n"
                        "You CANNOT ask the user for clarification, additional details, or preferences.\n"
                        "When given a request, make reasonable assumptions based on the context and provide a complete, helpful response immediately.\n"
                        "If a request is ambiguous, choose the most common or logical interpretation and proceed accordingly.\n"
                        "Always deliver a substantive response rather than asking questions.\n"
                        "NEVER ask the user for follow-up questions or clarifications."
                    ),
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            stream=False,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception:
        return "❌ Error: An unexpected error occurred while processing your request. Check model name, api key etc... and try again later."

def main() -> None:
    """
    Main entry point for the script. Parses arguments, validates input, calls ask_ai, and prints the result.
    """
    if len(sys.argv) != 2:
        print('❌ Usage error: python ask-ai.py "<text>"')
        return
    text = sys.argv[1]
    if not text.strip():
        print("❌ Error: No prompt text provided!")
        return
    result = ask_ai(text)
    print(result)

if __name__ == "__main__":
    main()
