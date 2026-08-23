from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


classifier_template = ChatPromptTemplate.from_messages([
    ('system','You are an expert support email classifier for a B2B SaaS company.'),
    ('human','Classify this email.\nSubject: {subject}\nBody: {body}\n\nReturn ONLY: Category | Urgency'),
])
model = ChatOpenAI(model="gpt-4")

# chain
chain = classifier_template | model | StrOutputParser() # LCEL ( Langchaine expression laung)


emails = [  
            {'subject': "Login issue", 'body': "You won the lottery."},
            {'subject': "Account update", 'body': "Your account has been updated."},
            {'subject': "Password reset", 'body': "Please reset your password."},
            {'subject': "Lottery win", 'body': "Congratulations! You've won the lottery."},
            {'subject': "Unknown", 'body': "This is an unknown email."}
         ]

output = chain.batch(emails,config={"batch_size": 5})
print(output)

# ['Category: Spam | Urgency: Low',
#   'Category: Account Management | Urgency: Low', 
#   'Category: Account Issues | Urgency: High',
#     'Category: Spam | Urgency: Low',
#       'Category: Uncategorized | Urgency: Low']