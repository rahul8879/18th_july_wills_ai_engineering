from openai import OpenAI

client = OpenAI()

def call_llm(email):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "Please classify the email into one of the category:  Spam, Not spam. Just give me category no thoery" + email
            }
        ]
    )

    return response.choices[0].message.content



emails =[
 "Hi Team, please click here to send the invoice",
 "HI team, I am not able to login to my account",
 "Hi team, please send me the invoice",
 "Hi Learnerm click here to get free course",
 "Hi Learnerm click here to get free course"
 "Hi Team, click here to get free openai key",
 "Hi team, click here to get pro subscription", 

]


for email in emails:
    print(call_llm(email))

# print(call_llm("Hi Team, please click here to send the invoice"))

