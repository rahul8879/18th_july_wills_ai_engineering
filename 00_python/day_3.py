
# data = ['python','llm','agentic ai','openai']
# for i in range(len(data)):
#     if 'llm' in data[i]:
#         print('found at index', i)
#         break
#     print('still trying to find', data[i])
# from utils import cleaning_output
# output = ['Billing | 0.9', 'Technical | 0.8', 'Login | 0.7', 'Account | 0.6']
# category, score = cleaning_output(output)
# print(category)
# print(score)

class BaseClass:
    def __init__(self):
        self.base_attribute = "I am a base attribute"
    def base_method(self):
        return "I am a method of the BaseClass"

class BankAccount(BaseClass):
    def __init__(self, account_number, account_holder):
        super().__init__()
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")



cust_1 = BankAccount(11, "John Doe")
cust_1.deposit(100)  # Deposited 100. New balance is 100.
# print(cust_1.deposit(100))  # 100
cust_1.deposit(100) 
cust_2 = BankAccount(12, "Rahul")
cust_2.deposit(50)  # Deposited 200. New balance is 200.