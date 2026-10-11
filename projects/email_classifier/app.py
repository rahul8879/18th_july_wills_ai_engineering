from model import call_llm
import os
from collections import Counter

def load_prompt(filename):
    path = os.path.join('prompts', filename)
    with open(path, 'r') as file:
        return file.read()


def classify_with_cot(subject,body):
    # 1. load the prompts
    template = load_prompt('classify_cot.md')
    prompt = template.format(subject=subject, body=body)
    # step 2. : call llm
    result = call_llm(prompt)
    # step 3 : extraction logic
    print(result.split('\n'))
    category, urgency = None, None
    for line in result.split('\n'):
        if 'CATEGORY' in line:
            category = line.split(':')[1].strip()
        if 'URGENCY' in line:
            urgency = line.split(':')[1].strip()
    return category, urgency



def classify_with_self_consistency(subject,body, nu_runs=8):
    # 1. load the prompts
    template = load_prompt('classify_cot.md')
    prompt = template.format(subject=subject, body=body)
    # step 2. : call llm multiple times
    results = []
    for _ in range(nu_runs):
        result = call_llm(prompt)
        for line in result.split('\n'):
            if 'CATEGORY' in line:
                results.append(line.split(':')[1].strip())

    votes = Counter(results)
    winner = votes.most_common(1)[0]
    confidence = winner[1] / nu_runs

    return {
        'votes': votes,
        'category': winner[0],
        'confidence': confidence
    }

        
def draft_response_with_tot(subject, body, category):
    # Load the prompt
    template = load_prompt('tree_of_thoughts.md')
    prompt = template.format(subject=subject, body=body, category=category)

    results = call_llm(prompt)

    return results



# subject = "Not happy"
# body = "I am not happy with the service I received. The product was defective and the support team was unhelpful. I want a refund immediately."
# # category, urgency = classify_with_cot(subject, body)

# # print('result from cot:', category, urgency)

# # print('result from self-consistency:', classify_with_self_consistency(subject, body))
# print('output from tot:', draft_response_with_tot(subject, body, 'Billing'))


# # ['CATEGORY: Billing\nURGENCY: High',
# #   'CATEGORY: Billing\nURGENCY: High', 
# #   'CATEGORY: Billing\nURGENCY: High', 
# #  'CATEGORY: Billing\nURGENCY: High',
# #    'CATEGORY: Billing\nURGENCY: High']