from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_gemini import Chat
import time
load_dotenv()

llm_1 = ChatOpenAI(model="gpt-4")
hf_llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    provider="novita"
)

llm_2 = ChatHuggingFace(llm=hf_llm)

# llm_3 = ChatGemini(model="gemini-1.5-turbo",api_key="")
start_time = time.time()
print("LLM 1:", llm_1.invoke('Tell me about India').content)
end_time = time.time()
print("LLM 1 response time:", end_time - start_time) #12.680685997009277

start_time = time.time()
print("LLM 2:", llm_2.invoke('Tell me about India').content)
end_time = time.time()
print("LLM 2 response time:", end_time - start_time) 
# print('type of response from llm1 ',type(llm_1.invoke('hi')))
# print('type of response from llm2 ',type(llm_2.invoke('who are you')))
