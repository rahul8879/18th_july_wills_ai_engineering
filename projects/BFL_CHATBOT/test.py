from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,  # need to discuss this in the future
)


ROUTER_PROMPT = """
You are a query classifier for Bajaj Finance helpdesk.

Classify the customer query into ONE of these categories:
- "tool"   : query requires live loan data (needs Loan ID like BFL001)
              Examples: loan status, EMI schedule, prepayment, refund,
              foreclose my loan, close my loan, settle my account
- "policy" : query is about rules, eligibility, charges, documents
              AND follow-up questions about a previous policy answer
              Examples: CIBIL score, foreclosure charges, interest rates,
              documents needed, what happens if I miss EMI,
              "how do you know this", "where did you get this",
              "is this from your policy", "what is your source"
- "general": greeting, thank you
- "blocked" : anything outside to finance or BFL chatbot

Reply with ONLY one word: tool / policy / general
"""

def classify_query(query):
    response = llm.invoke([
        SystemMessage(content=ROUTER_PROMPT),
        HumanMessage(content=query),
    ])
    category = response.content.strip()
    if category not in ["tool", "policy", "general", "blocked"]:
        raise ValueError(f"Invalid category: {category}")
    return category


print(classify_query("please help me to write a python code to add two number"))