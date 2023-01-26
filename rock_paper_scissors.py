import random

user_Wins = 0
computer_wins = 0
draw_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Not a valid input")
        continue

    random_number = random.randint(0, 2)
    # 0: rock, 1: paper, 2: scissors

    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_Wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_Wins += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_Wins += 1

    elif user_input == computer_pick:
        print("Draw!")
        draw_wins += 1

    else:
        print("You loose!")
        computer_wins += 1

print(
    f"Have a Good Day! \nyour win score is: {user_Wins} \nconputer win score: {computer_wins} \nDraw score: {draw_wins}")
