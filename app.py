import argparse
import os
from pathlib import Path
from typing import Optional

from google import genai
from google.genai import types

DEFAULT_MODEL = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """
You are a business writing assistant.

Your job is to turn raw meeting notes into:
1. structured action items
2. a professional follow-up email

Rules:
- Use only the information provided in the notes
- Do not invent names, dates, decisions, or approvals
- If information is missing or unclear, write: "Unclear - needs human review"
- Keep the output professional, concise, and easy to scan
"""

DEFAULT_NOTES = """
Team discussed launching the new app feature next Friday.
Sarah will finish the draft by Tuesday.
Kevin will review the budget.
The team also wants a short update sent to leadership.
""".strip()


def load_notes(input_file: Optional[str]) -> str:
    if input_file:
        return Path(input_file).read_text(encoding="utf-8").strip()
    return DEFAULT_NOTES


def build_prompt(notes: str) -> str:
    return f"""
Meeting notes:
{notes}

Please produce exactly these two sections.

Section A: Action Items
For each action item, include:
- Owner
- Task
- Deadline
- Clarity note

Section B: Follow-Up Email
Include:
- Subject
- Email body

Important:
- If owner, deadline, or decision is not clear, write "Unclear - needs human review"
- Do not add facts that are not in the notes
"""


def generate_output(notes: str, model: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "No API key found. Set GEMINI_API_KEY in your terminal before running the script."
        )

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=build_prompt(notes),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        ),
    )

    if not response.text:
        raise RuntimeError("The model returned an empty response.")

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Turn meeting notes into action items and a follow-up email."
    )
    parser.add_argument(
        "--input-file",
        type=str,
        default=None,
        help="Optional path to a .txt file containing meeting notes.",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default="output.txt",
        help="Path to save the generated output.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help="Gemini model name to use.",
    )

    args = parser.parse_args()

    notes = load_notes(args.input_file)
    output = generate_output(notes, args.model)

    Path(args.output_file).write_text(output, encoding="utf-8")

    print("=== GENERATED OUTPUT ===")
    print(output)
    print(f"\nSaved to: {args.output_file}")


if __name__ == "__main__":
    main()
