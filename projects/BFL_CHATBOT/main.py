from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from tools import get_loan_status, get_emi_schedule
from langchain_core.chat_history import InMemoryChatMessageHistory
import uuid
from typing import Optional
from rag_chain import rag_answer
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None  # Optional session ID for maintaining chat history

class ChatResponse(BaseModel):
    reply: str
    session_id: str
    tools_called: list[str] = []


app = FastAPI(title="BFL Chatbot API",
               description="API for BFL Chatbot", 
               version="1.0.0")



llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,  # need to discuss this in the future
)


TOOLS = [get_loan_status, get_emi_schedule]
llm_with_tools = llm.bind_tools(TOOLS)

tool_map = {
        "get_loan_status": get_loan_status,
        "get_emi_schedule": get_emi_schedule
    }


# Phase 1 : development started


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
    if category not in ["tool", "policy", "general", 'blocked']:
        raise ValueError(f"Invalid category: {category}")
    return category















SYSTEM_PROMPT = """You are a professional Bajaj Finance customer support agent.

You have access to:
1. TOOLS  — for live loan data (status, EMI, prepayment, refund)
             Use when customer provides a Loan ID (BFL + digits)
2. POLICY — handled separately via knowledge base

RULES:
- Loan ID present → use tools
- Format all amounts with Rs and commas (e.g., Rs 8,450)
- Be warm, concise, and professional
- If a loan is not found, ask customer to double-check the Loan ID
"""
store = {}
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """Return existing chat history or create a new one for this session."""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

def run_chat_turn(user_message: str, session_id: str) -> str:
    history = get_session_history(session_id)
    messages = [{'role':"system","content":SYSTEM_PROMPT}]
    messages.extend(history.messages)
    messages.append(HumanMessage(content=user_message))
    tools_used = []

    response = llm_with_tools.invoke(messages)

    while response.tool_calls:
        messages.append(response)
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tools_used.append(tool_name)

            tool_fn = tool_map.get(tool_name)
            if tool_fn:
                result = tool_fn.invoke(tool_args)
            else:
                result = {"error":"tool is not available"}

            messages.append(ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]

            ))
        response = llm_with_tools.invoke(messages)

    history.add_user_message(user_message)
    history.add_ai_message(response.content)

    return response.content, tools_used


# 
def run_policy_run(user_message,session_id):
    history = get_session_history(session_id)
    policy_history = history.messages
    reply = rag_answer(user_message, policy_history)
    history.add_user_message(user_message)
    history.add_ai_message(reply)
    return reply

def run_general_turn(user_message:str,session_id):
    history = get_session_history(session_id)
    message = [{'role':"system","content":SYSTEM_PROMPT}]
    message.extend(history.messages)
    message.append(HumanMessage(content=user_message))
    response = llm.invoke(message)
    history.add_user_message(user_message)
    history.add_ai_message(response.content)
    return response.content
    

    

    

@app.get("/ui")
def read_root():
    return HTMLResponse(content=open("home.html").read(), status_code=200)

@app.post("/chat",response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    session_id = str(uuid.uuid4())

    # step 1 : classify the query 
    query_type = classify_query(request.message)
    print(f"Query Type: {query_type}")
    if query_type == "tool":
        reply, tool_called = run_chat_turn(request.message,request.session_id)
        return ChatResponse(reply=reply, session_id=session_id, tools_called=tool_called,
                            query_type=query_type)
    
    elif query_type == "policy":

        reply = run_policy_run(request.message, request.session_id)
        print(f"Policy Reply: {reply}")
        return ChatResponse(reply=reply, session_id=session_id, query_type=query_type)

    elif query_type == "general":
        reply = run_general_turn(request.message, request.session_id)
        return ChatResponse(reply=reply, session_id=session_id, query_type=query_type)
    else:
        return ChatResponse(reply="We are sorry, I can't assist with that.", session_id=session_id, query_type=query_type)



# @app.post("/history")
# def history_endpoint():
#     # Here you would retrieve the chat history
#     history = [
#         {"user": "Hello", "bot": "Hi there!"},
#         {"user": "How are you?", "bot": "I'm just a bot, but thanks for asking!"}
#     ]
#     return {"history": history}
