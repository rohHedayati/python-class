# Menu
# 1: Check prime number
# 2: Check complete(Perfect) number
# 3: Check odd or even number
# 4: Positive or negative number
# 5: Cal number digits 
# 6: Cal sum of number digits
# 0: exit


def menu():
    print("1: Check prime number")
    print("2: Check complete(Perfect) number")
    print("3: Check odd or even number")
    print("4: Positive or negative number")
    print("5: Cal number digits")
    print("6: Cal sum of number digits")
    print("0: exit")
    choice = int(input("Enter your choice:"))
    # while choice < 0 or choice > 6:
    #     print("Wrong choice. try again.")
    #     choice = int(input("Enter your choice:"))

    while choice not in list(range(7)):
        print("Wrong choice. try again.")
        choice = int(input("Enter your choice:"))
    return choice

def prime_num(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    if is_prime == True:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")

def perfect_num(num):
    sum_num = 0
    for x in range(1,num):
        if num % x == 0:
            sum_num += x
    if sum_num == num:
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not perfect number")

def odd_even(num):
    pass
def sign_num(num):
    pass
def count_digit(num):
    pass
def sum_digit(num):
    pass

while True:
    print("==============================================")
    x = menu()
    number = int(input("Enter a number:"))
    if x == 1:
        prime_num(number)
    elif x == 2:
        perfect_num(number)
    elif x == 3:
        odd_even(number)
    elif x == 4:
        sign_num(number)
    elif x == 5:
        count_digit(number)
    elif x == 6:
        sum_digit(number)
    else:
        break