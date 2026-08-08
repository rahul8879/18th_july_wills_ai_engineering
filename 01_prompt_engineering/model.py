from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

prompt = "Please classify my email : Hi team I am facing the login issue"

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("AI Response",response.choices[0].message.content)

