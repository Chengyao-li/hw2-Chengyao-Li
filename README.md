# Week 2 GenAI Workflow

## Business Workflow
This project uses an LLM to turn raw meeting notes into:
1. action items
2. a short follow-up email

## User
A project coordinator or team member who needs quick written follow-up after meetings.

## Input
Unstructured meeting notes.

## Output
A structured action-item list and a professional follow-up email draft.

## Why this is valuable
This task is repetitive, time-consuming, and writing-heavy, so it is a good candidate for partial automation.

## How to Run
Install dependency:
python -m pip install -U google-genai

Set your Gemini API key in the environment.

Run:
python app.py

Or run with your own notes:
python app.py --input-file sample_notes_1.txt --output-file result1.txt

## Video Walkthrough
[Paste your unlisted YouTube or Vimeo link here]
