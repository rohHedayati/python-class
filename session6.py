import random

rounds = 5
user_scores = 0
computer_scores = 0
password = '123'
incorrect_count = 2

print("----------------Welcome to game----------------")
name = input("Enter Your name:")
pass_word = input("Enter password:")
while pass_word != password and incorrect_count > 0:
    incorrect_count -= 1
    print("Password incorrect!")
    pass_word = input("Enter password:")

if incorrect_count > 0:
    for i in range(rounds):
        print(f"===========Round {i+1} / {rounds}===========")
        print("1: For Scissor")
        print("2: For Rock")
        print("3: For Paper")
        user_choice = int(input("Enter your choice:"))
        
        # user_choice = int(input("1: For Scissor\n2: For Rock\n3: For Paper\nEnter your choice:"))
        computer_choice = random.randint(1,3)
        print(f"Computer choice: {computer_choice}")
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
        print(f'{name} Wins: {user_scores}  ----  Computer Wins: {computer_scores}')
        print('-------------------------------------------------')

else:
    print("You are Ban!")
    print("Bye!")



