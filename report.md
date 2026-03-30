# Report
# Report

## Business Use Case
This prototype supports a common business writing workflow: turning raw meeting notes into action items and a follow-up email. The likely user is a project coordinator, team lead, or operations assistant who needs to convert unstructured notes into clear written communication quickly.

## Model Choice
I used Gemini because it was easy to access through Google AI Studio and simple to connect through Python. It worked well for a lightweight prototype and made it easy to test multiple prompt versions.

## Baseline vs Final Design
The baseline prompt produced usable drafts for straightforward cases, but it sometimes filled in unclear details too confidently. After prompt iteration, I added stronger instructions not to invent names, dates, or decisions, and I required the model to mark unclear items for human review. In the final version, I also used a fixed structure for action items and the follow-up email. This made the output more consistent, safer, and easier to evaluate.

## Remaining Failure Cases
The prototype still struggles when notes are incomplete, fragmented, or vague. In those cases, it may still produce wording that sounds more certain than the original notes justify. Human review is still necessary before sending any message to a client, manager, or external stakeholder.

## Deployment Recommendation
I would recommend this workflow only as a draft-generation tool, not as a fully automated system. It is useful for saving time on repetitive writing, but outputs should still be reviewed by a human before use, especially when the notes are ambiguous or the communication is high-stakes.
