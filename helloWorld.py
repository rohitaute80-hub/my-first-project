import random
print("Hello, welcome to Rock, Papper, Scissors Game!")
first = input("Enter your choice (rock, paper, scissors): ")
options = ["rock", "paper", "scissors"]
second = random.choice(options)
print(random.choice(options))
if first == second:
    print("It's a tie!")
elif (first == "rock" and second == "scissors") or (first == "paper" and second == "rock") or (first == "scissors" and second == "paper"):
    print("You win!")   
else:    print("You lose!")