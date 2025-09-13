# Menu
# 1: Check prime number
# 2: Check complete(Perfect) number
# 3: Check odd or even number
# 4: Positive or negative number
# 5: Cal number digits 
# 6: Cal sum of number digits
# 7: Reverse number digits
# 8: Guess number game
# 0: exit


def menu():
    print("1: Check prime number")
    print("2: Check complete(Perfect) number")
    print("3: Check odd or even number")
    print("4: Positive or negative number")
    print("5: Cal number digits")
    print("6: Cal sum of number digits")
    print("7: Reverse number digits")
    print("8: Guess number game")
    print("0: exit")
    choice = int(input("Enter your choice:"))
    # while choice < 0 or choice > 6:
    #     print("Wrong choice. try again.")
    #     choice = int(input("Enter your choice:"))

    while choice not in list(range(9)):
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
    if num % 2:
        print(f"{num} is odd")
    else:
        print(f"{num} is even")

def sign_num(num):
    if num > 0:
        print(f"{num} is positive(+)")
    elif num < 0:
        print(f"{num} is negative(-)")
    else:
        print(f"{num} is zero(0)")

def count_digit(num):
    print(f"{num} has {len(str(num))} digits")

def sum_digit(num):
    s = 0
    n = num
    while num != 0:
        r = num % 10
        s += r
        num = num // 10
    print(f"Sum of {n} digits = {s}")

def reverse_number(num):
    print(f"Reverse of {num} is {str(num)[::-1]}")

def guess_number():
    import random
    max_attempts = 5
    # is_correct = False
    num = random.randint(1,100)
    for x in range(max_attempts):
        print(f"Attempt {x+1} / {max_attempts}")
        user_choice = int(input("Enter your guess:"))
        if user_choice > num:
            print("your choice is greater than number")
        elif user_choice < num:
            print("your choice is less than number")
        else:
            print("Well done!")
            # is_correct = True
            break
    else:
        print("You lose")

    # if not is_correct:

def sum_of_digits(num, type):
    pass

sum_of_digits(1456, 'all')
sum_of_digits(1456, 'even')
sum_of_digits(1456, 'odd')
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
    elif x == 7:
        reverse_number(number)
    elif x == 8:
        guess_number()
    else:
        break