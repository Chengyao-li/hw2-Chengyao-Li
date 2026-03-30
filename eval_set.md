# Evaluation Set

## Case 1: Normal case
**Input:**  
Team discussed launching the new app feature next Friday. Sarah will finish the draft by Tuesday. Kevin will review the budget. The team also wants a short update sent to leadership.

**Good output should:**  
Clearly identify owners, deadlines, and produce a concise professional follow-up email.

## Case 2: Normal case
**Input:**  
Marketing meeting notes: finalize poster copy, confirm event room, send reminder email to students, and prepare sign-up sheet. Anna handles the poster, Mike handles the room, and Jenny sends the reminder by Wednesday.

**Good output should:**  
Turn notes into organized action items and a clear email without missing responsibilities.

## Case 3: Edge case
**Input:**  
We should probably finish the report soon. Someone needs to talk to finance. Maybe next week works for the client meeting.

**Good output should:**  
Acknowledge ambiguity, avoid inventing names or dates, and flag unclear items for review.

## Case 4: Human review / hallucination risk
**Input:**  
The client agreed to the pricing change and legal approved the contract yesterday.

**Good output should:**  
Avoid overstating certainty if details are incomplete and avoid fabricating contract details.

## Case 5: Messy input
**Input:**  
notes: website bug homepage broken / ask dev? maybe sam / invoice unpaid / client angry / send apology today / demo move fri maybe 3pm

**Good output should:**  
Handle fragmented notes, keep uncertainty visible, and produce a usable first draft.
