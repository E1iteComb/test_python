import random

choice = random.randint(1,3)
computer = ""

if choice == 1:
    computer = "rock"
elif choice == 2:
    computer = "paper"
elif choice == 3:
    computer = "scissors"

print("Welcome to Rock-Paper-Scissors!")

player_choice = input("Enter rock, paper, or scissors: ")
print("You chose:", player_choice)
print(f"Computer chose: {computer}")
