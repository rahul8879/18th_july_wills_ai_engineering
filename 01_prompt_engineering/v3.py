from model import call_llm

examples_block = f"""
EXAMPLE 1: 
Subject: Charged $299 instead of $99
Body: I was charged $299 for my subscription, but I signed up for the $99 plan. Can you help me resolve this?
Output: {{
    "category": "billing",
    "urgency": "high",
    "billing_sub": "incorrect_charge"
}}

EXAMPLE 2:
Subject: Unable to access my account
Body: I'm having trouble logging into my account. I've tried resetting my password, but I still can't get in.
Output: {{
    "category": "account",
    "urgency": "medium",
    "billing_sub": "access_issue"
}}

EXAMPLE 3:
Subject: Feature request for bulk invoicing
Body: Hi, I'd like to request a feature that allows for bulk invoicing. It would save us a lot of time.
Output: {{
    "category": "feature_request",
    "urgency": "low",
    "billing_sub": "bulk_invoicing"
}}
"""

email_subject = "Charged $299 instead of $99"
email_body = "I was charged $299 for my subscription, but I signed up for the $99 plan. Can you help me resolve this?"

template = f"""
CRITICAL: Return ONLY valid JSON. No explanation. No markdown.

# ROLE
You are a support email classifier for a B2B SaaS company with deep 
knowledge of our product and customer patterns.

# EXAMPLES OF CORRECT CLASSIFICATIONS
Study these examples carefully — they reflect OUR specific business context:
{examples_block}

# NOW CLASSIFY THIS EMAIL
Subject: {email_subject}
Body: {email_body}

REMINDER: Return ONLY the JSON. Exactly 3 fields: category, urgency, billing_sub.
"""

response = call_llm(template)

print(response)
