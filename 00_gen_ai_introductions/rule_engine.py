

billing = ['billing','payment','invoice','charge','refund']
technical = ['login','error','bug','issue','problem']
feature_request = ['feature','request','enhancement','improvement','suggestion']



def classify_email(email):
    email_lower = email.lower()
    for word in billing:
        if word in email_lower:
            return "Billing"
    for word in technical:
        if word in email_lower:
            return "Technical"
    for word in feature_request:
        if word in email_lower:
            return "Feature Request"
    return "Other"


emails = ["bill  with  #123", "Login failed for user admin", "Feature request for dark mode"]

output = []

for i in emails:
    category = classify_email(i)
    output.append(category)

print(output)
