balance = 0
transactions = []
# salary
# 150000000
# 14040631
# 
def income():
    global transactions
    global balance
    t = input("Enter income title:")
    p = int(input("Enter income price(Rial):"))
    d = input("Enter income date(14040631):")
    income_transaction = {
        "title": t,
        "price": p,
        "date": d,
        "type": 'income'
    }
    transactions.append(income_transaction)
    balance += p
    print("Income added!")

def expense():
    pass

def show():
    print(transactions)
    print(f"Your account balance: {balance:,.2f} Rial")

def first_balance(x):
    global balance
    balance = x
    print(f"Your account balance: {balance:,.2f} Rial")

def menu():
    print("-"*50)
    print("Enter 1: First account balance:")
    print("Enter 2: Add income:")
    print("Enter 3: Add expense:")
    print("Enter 4: Show transactions list:")
    print("Enter 0: To exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        b = int(input("Enter your first balance (Rial):"))
        first_balance(b)
    elif ch == 0:
        return
    elif ch == 2:
        income()
    elif ch == 3:
        expense()
    elif ch == 4:
        show()

    menu()



menu()




# try:
#     x = int(input("Enter x:"))
#     y = 10/x
#     print(x)
# except Exception as error:
#     print(f"{type(error)}: {error}")
# else:
#     print("Else Block")
# finally:
#     print("Final Block")
# except (ValueError, IndexError):
#     print("Enter valid number")
# except ZeroDivisionError:
#     print("Enter number>0")
