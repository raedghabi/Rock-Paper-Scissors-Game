import random 
imojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
continue_options = ['y', 'n']
choices = ['r', 'p', 's']
def ask_to_continue():
    while True: 
        cont = input("continue? (y/n) :").lower()
        if cont not in continue_options:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        elif cont == 'n':
            print("Thanks for playing!")
            exit()
        else:
            return cont

while True :
    user_choice = input("Enter rock, paper, or scissors or (r, p, s) and  ( 'q' to quit): ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid input. Please enter rock, paper, or scissors (r, p, s).")
        continue
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        print(f"Computer chose: {imojis[computer_choice]}")
        print(f"You chose: {imojis[user_choice]}")
        print("It's a tie!")
        ask_to_continue()
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print(f"Computer chose: {imojis[computer_choice]}")
        print(f"You chose: {imojis[user_choice]}")
        print("You win!")
        ask_to_continue()
    else:
        print(f"Computer chose: {imojis[computer_choice]}")
        print(f"You chose: {imojis[user_choice]}")
        print("Computer wins!")
        ask_to_continue()