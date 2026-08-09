from model import call_llm

template = """
Please classify the below email 
{email}
Category should be only below type
- Technical
- Billing
- General Inquiry
Output should look like below
Category
"""
prompt = template.format(email="I need to update my payment method for the subscription.")

# prompt = "Please classify my email : Hi team I am facing the login issue"
output = call_llm(prompt)
print(output)