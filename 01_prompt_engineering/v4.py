from model import call_llm

PRODUCT_CONFIGS = {
    "saas_crm": {
        "product_name": "CRM Platform",
        "categories": ["Billing", "Technical", "Feature Request", "Spam", "Other"],
        "urgency_levels": ["High", "Medium", "Low"],
        "sla_hours": {"High": 2, "Medium": 8, "Low": 24},
        "examples": [
            {"subject": "SFDC not syncing", "body": "Salesforce stopped pulling leads",
             "output": {"category": "Technical", "urgency": "High"}}
        ]
    },
    "fintech_payments": {
        "product_name": "Payment Gateway",
        "categories": ["Transaction Failed", "Fraud Alert", "Settlement Delay", "KYC Issue", "Other"],
        "urgency_levels": ["Critical", "High", "Medium"],
        "sla_hours": {"Critical": 1, "High": 4, "Medium": 12},
        "examples": [
            {"subject": "Payment declined at checkout", "body": "Card declined even though sufficient balance",
             "output": {"category": "Transaction Failed", "urgency": "High"}}
        ]
    },
    "edtech": {
        "product_name": "EdTech Platform",
        "categories": ["Enrollment Issue", "Course Access", "Payment Issue", "Other"],
        "urgency_levels": ["Critical", "High", "Medium"],
        "sla_hours": {"Critical": 1, "High": 4, "Medium": 12},
        "examples": [
            {"subject": "Payment declined at checkout", "body": "Card declined even though sufficient balance",
             "output": {"category": "Payment Issue", "urgency": "High"}}
        ]
    }
}


# print(PRODUCT_CONFIGS['fintech_payments']['categories'])


template = """
You are email classifier at {product_name}.
Classify into one of the category:
{categories}

email: {email}
REMINDER: Return ONLY the JSON. Exactly 3 fields: category, urgency, billing_sub. """

email = input("Enter the email body: ")
product_name = input("Enter the product name: ")
categories = PRODUCT_CONFIGS[product_name]['categories']

prompt = template.format(product_name=product_name, categories=categories, email=email)

response = call_llm(prompt)
print(response)