import random
user_scores = 0
computer_scores = 0
rounds = int(input("Enter rounds of the game:"))

def user_select():
    print("1: For Scissor")
    print("2: For Rock")
    print("3: For Paper")
    user_choice = int(input("Enter your choice:"))
    return user_choice

def computer_select():
    computer_choice = random.randint(1,3)
    print(f"Computer choice: {computer_choice}")
    return computer_choice

def compare(user_choice, computer_choice):
    global user_scores
    global computer_scores
    if (user_choice == 1 and computer_choice == 3) or \
        (user_choice == 2 and computer_choice == 1) or \
        (user_choice == 3 and computer_choice == 2):
        user_scores += 1
        print("User Win!")
    elif user_choice == computer_choice:
        print("Tie!")
    else:
        computer_scores += 1
        print("Computer Win!")

print("----------------Welcome to game----------------")
name = input("Enter Your name:")

for i in range(rounds):
    print(f"===========Round {i+1} / {rounds}===========")
    user_choice = user_select()
    computer_choice = computer_select()
    compare(user_choice, computer_choice)

    print(f'{name} Wins: {user_scores}  ----  Computer Wins: {computer_scores}')
    print('---------------------------------------------------------------------')



