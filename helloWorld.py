import random

print("Let's play Rock, Paper, Scissors")
first = input("Player 1, please enter your choice: Rock, Paper or Scissors: ")
options = ["Rock", "Paper", "Scissors"]

if first not in options:
    print("Invalid choice, please choose Rock, Paper or Scissors")
else:
    second = random.choice(options)
    print("Player 2 chooses:", second)

    if first == "Rock":
        if second == "Rock":
            print("It's a tie!")
        elif second == "Paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif first == "Paper":
        if second == "Rock":
            print("Player 1 wins!")
        elif second == "Paper":
            print("It's a tie!")
        else:
            print("Player 2 wins!")
    elif first == "Scissors":
        if second == "Rock":
            print("Player 2 wins!")
        elif second == "Paper":
            print("Player 1 wins!")
        else:
            print("It's a tie!")

