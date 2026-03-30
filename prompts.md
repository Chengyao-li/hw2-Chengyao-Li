# Prompt Iteration

## Initial Version
You are a helpful business writing assistant.
Turn the meeting notes into:
1. a list of action items
2. a professional follow-up email

Keep the tone clear and concise.
Do not include information that is not in the notes.

**What changed and why:**  
This was the starting version. It was simple, but it did not clearly tell the model how to handle unclear or incomplete information.

**What improved / stayed the same / got worse:**  
It could produce usable drafts for clean inputs, but it sometimes sounded too confident when the notes were ambiguous.

---

## Revision 1
You are a business writing assistant.
Convert meeting notes into:
1. structured action items
2. a concise professional follow-up email

Rules:
- Do not invent names, dates, or decisions
- If an item is unclear, mark it as "Needs human review"
- Keep the email professional and concise

**What changed and why:**  
I added explicit rules to reduce hallucination and make the model flag unclear details instead of guessing.

**What improved / stayed the same / got worse:**  
This version handled ambiguous cases better and reduced made-up details, but the output structure was still not always consistent.

---

## Revision 2
You are a business writing assistant.
Based only on the notes provided, produce:

Section A: Action Items
- Owner
- Task
- Deadline
- Clarity note

Section B: Follow-Up Email
- Subject line
- Email body

Rules:
- Use only information in the notes
- If owner or deadline is missing, say "Unclear - needs human review"
- Do not invent facts
- Keep output easy to scan

**What changed and why:**  
I added a fixed output structure so the results would be easier to compare and safer to review.

**What improved / stayed the same / got worse:**  
This version gave the most consistent and readable output. It was easier to evaluate, although the writing sounded slightly less natural than the earlier version.
