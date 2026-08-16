from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    return response.choices[0].message.content

