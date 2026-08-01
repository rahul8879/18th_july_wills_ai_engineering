from utils import sales_comparison, test

# sales_data = [100]
# output = sales_comparison(sales_data)

# print(output)

# toxic_text ="You are very bad person, I really hate you!"
# if 'BAD'.lower() in toxic_text.lower():
#     print("Toxic content detected.")
# else:
#     print("No toxic content detected.")

template ="""
Classify the below email 
Subject: {subject}
Body: {body}
"""

# prompt = template.format(subject="Login Issue", body="I am facing the login issue with the application.")
# print(prompt)


# model_1_output = "This is a login issue email."
# model_2_output = "This is a technical issue email."

# summary = model_1_output+'---'+model_2_output
# print(summary)

# output = "I am dummy text"

# model = f"Hey here is your output: {output}"
# print(model)

for i in [23,34,56]:
    if i==34:
        print("Found 34!")
        break
    print(i)

print(" I am done with the process")