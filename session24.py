balance = 0
transactions = []

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
        "type": '+'
    }
    transactions.append(income_transaction)
    balance += p
    print("Income added!")

def expense():
    global transactions
    global balance
    t = input("Enter expense title:")
    p = int(input("Enter expense price(Rial):"))
    d = input("Enter expense date(14040631):")
    expense_transaction = {
        "title": t,
        "price": p,
        "date": d,
        "type": '-'
    }
    transactions.append(expense_transaction)
    if balance < p:
        print("Not enough money!")
        return
    balance -= p
    print("expense added!")

def show():
    global transactions
    row_col = "Row"
    title_col = "Title"
    date_col = "Date"
    price_col = "Price"
    type_col = "Type"
    heading_title = "Transactions List"
    print('='*80)
    print(f"{heading_title:^80}")
    print('='*80)
    print(f"{row_col:^10}|{title_col:^20}|{date_col:^12}|{price_col:^20}|{type_col:^10}")
    print('-'*80)
    for (i, x) in enumerate(transactions):
        print(f"{i:^10}|{x['title']:^20}|{x['date']:^12}|{x['price']:^20,}|{x['type']:^10}")
    print('-'*80)
    print(f"Your account balance: {balance:,.2f} Rial")

def first_balance(x):
    global balance
    global transactions
    balance = x
    tr = {
        "title": 'First Balance',
        "price": x,
        "date": '00000000',
        "type": '*'
    }
    transactions.append(tr)
    print(f"Your account balance: {balance:,.2f} Rial")

def menu():
    print("-"*80)
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
# x = 100000
# y = "title"
# print(f"{y:<20}{x:^12,}")
# print("title:<20")
