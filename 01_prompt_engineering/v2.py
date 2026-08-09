from model import call_llm

with open("classify_basic.md", "r") as file:
    template = file.read()

prompt = template.format(body="Hi Team I am not able to login into my account.I have paid my bill.")

print(call_llm(prompt))
