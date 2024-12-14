import random

option = ("rock","paper","scissers")
guess = None
palyer =input("Enter a choice (rock,paper,scissers) ")
computer = random.choice(option)

while palyer not in option :
    palyer = input("Enter a choice (rock,paper,scissers) ")

print(f"palyer: {palyer}")
print(f"computer: {computer}")

if palyer == computer:
    print("It's a tie :")

elif palyer == "rock" and computer == "scissers":
    print("you win")

elif palyer == "scissers" and computer == "paper" :
    print("you win")

elif palyer == "paper" and computer == "rock" :
    print("you win")
else:
    print("you lose")
