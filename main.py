import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nPlease choose: \n\t\trock, paper, scissors or Q to quit game: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("You did not choose one of the options")
        continue

    random_number = random.randint(0, 2)

    # 0=rock, 1=paper, 2=scissors

    computer_pick = options[random_number]

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You win!")


    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You win!")


    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You win!")


    elif user_input == "paper" and computer_pick == "paper":

        print("No points, you tied!")

    elif user_input == "rock" and computer_pick == "rock":

        print("You win!")

    elif user_input == "scissors" and computer_pick == "scissors":

        print("You win!")


    else:
        print("You lost!")
        computer_wins += 1

if computer_wins < user_wins:
    print("Sorry, you didn't win this time. \nThe computer's score was", computer_wins, "\nYour score was", user_wins)

elif computer_wins == user_wins:

    print("You and the computer tied!  \nThe computer's score was", computer_wins, "\nYour score was also", user_wins)


else:
    print("Congratulations! You won! \nThe computer's score was", computer_wins, "\nYour score was", user_wins)
print("Goodbye!")
