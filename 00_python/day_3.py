
# data = ['python','llm','agentic ai','openai']
# for i in range(len(data)):
#     if 'llm' in data[i]:
#         print('found at index', i)
#         break
#     print('still trying to find', data[i])
from utils import cleaning_output
output = ['Billing | 0.9', 'Technical | 0.8', 'Login | 0.7', 'Account | 0.6']
category, score = cleaning_output(output)
print(category)
print(score)


