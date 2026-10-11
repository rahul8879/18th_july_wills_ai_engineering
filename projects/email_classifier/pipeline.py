from app import classify_with_cot, classify_with_self_consistency, draft_response_with_tot

def is_pro_subscription(sender):
    pro_domain = ["bigclient.com", "enterprise.com", "corp.com"]
    domain = sender.split('@')[-1]
    return domain in pro_domain

def process_emails(email):
    # step 1 : classify the email using COT
    intial = classify_with_cot(email['subject'], email['body'])
    # step 2 : check if customer belongs to pro subscriptions ??
    is_pro = is_pro_subscription(email['sender'])
    # step 3 : if  pro, then classify using self consistency
    if is_pro:
        print(' pro subscription customer ')
        final = classify_with_self_consistency(email['subject'], email['body'])
    else:
        final = intial
    return final

emails = [
    {
        'sender': 'user@bigclient.com',
        'subject': 'Need help with my account',
        'body': 'I am having issues accessing my account. Please assist.'
    },
    {
        'sender': 'user@smallclient.com',
        'subject': 'Question about billing',
        'body': 'Can you provide details about my last invoice?'
    },
    {
        'sender': 'user@gmail.com',
        'subject': 'Urgent: Account issue',
        'body': 'I need immediate assistance with my account.'
    }
]


results = []

for email in emails:
    result = process_emails(email)
    results.append(result)

print('final results:', results)
