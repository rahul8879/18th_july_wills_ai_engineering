# step 1 : model
from model import call_llm


# step 2 : write your template
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

# you need your data ??