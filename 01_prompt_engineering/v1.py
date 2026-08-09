# step 1 : model
from model import call_llm
import pandas 
# step 2 : write your template
template = """
Please classify the below email 
{email}
Category should be only below type
- Technical
- Billing
- General Inquiry

Rules:
- Return ONLY the category name and confidance score ( between 1-10). Nothing else.
- No explanation, no punctuation, no extra words.
- If unsure, return "Other".

OUTPUT FORMAT
CATEGORY | CONFIDANCE SCORE

"""

# you need your data ??
# step 3 : we loaded the data
data = pandas.read_excel("emails.xlsx")

# we are just interested in email's body
emails = list(data['Body'])

# print(emails[:10])
output = []
for i in emails[:5]:
    prompt = template.format(email=i)
    output.append(call_llm(prompt))


print(output)

# data['model_output'] = output

# # save the entire files to local 
# data.to_csv("final-result.csv")