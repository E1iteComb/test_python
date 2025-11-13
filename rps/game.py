import random

print("Welcome to Rock-Paper-Scissors!")

choice = random.randint(1,3)
computer = ""

if choice == 1:
    computer = "rock"
elif choice == 2:
    computer = "paper"
elif choice == 3:
    computer = "scissors"

print(f"Computer chose: {computer}")