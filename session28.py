class Account:
    def __init__(self, n_id, acc_id):
        self.national_id = n_id
        self.account_id = acc_id
        self.balance = 0
        self.transactions = []
    
    def __str__(self):
        return f"Account : {self.account_id}, National_id: {self.national_id}, Balance : {self.balance}"

    def add_balance(self, amount):
        self.balance += amount
        x = {
            'amount': amount,
            'type': '+'
        }
        self.transactions.append(x)
        print(f"Account balance added: {amount}")
        print(self.show_balance())

    def sub_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            x = {
                'amount': amount,
                'type': '-'
            }
            self.transactions.append(x)
            print(self.show_balance())
            return
        print("Your balance is not enough!")

    def show_transactions(self):
        print("-"*70)
        print("List transaction")
        for x in self.transactions:
            print(f"{x['amount']:^20,}|{x['type']:^5}")
        print("-"*70)

    def show_balance(self):
        return f"Account balance = {self.balance}"
    


# account1 = Account('064999922', '100200300')
# print(account1)
# account1.add_balance(1000)
# account1.add_balance(4500)
# account1.sub_balance(500)
n_id = input("Enter national code:")
acc_id = input("Enter account id:")
account = Account(n_id, acc_id)
def menu():
    print("Enter 1: To add balance")
    print("Enter 2: To sub balance")
    print("Enter 3: To show transaction")
    print("Enter 0: To exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        amount = int(input("Enter amount(+):"))
        account.add_balance(amount)
    elif ch == 2:
        amount = int(input("Enter amount(-):"))
        account.sub_balance(amount)
    elif ch == 3:
        account.show_transactions()
    elif ch == 0:
        return
    else:
        print("Wrong option!")
    menu()

menu()