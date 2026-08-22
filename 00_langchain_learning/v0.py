from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")

simple_prompt = ChatPromptTemplate.from_template(
    'Reply in one sentence: {questions}'
)

chain = simple_prompt | chat | StrOutputParser()

questions = ["What is the capital of India?", "Who is the Prime Minister of India?", "What is the population of India?"]
for i in questions:
    print(chain.invoke({"questions": i}))