import random 
# generate a random number between 1 3 
program_number = random.randint(1,3)
program_choice = ""
if program_number == 1:
    program_choice = "Rock"
elif program_number == 2:
    program_choice = "Paper"
elif program_number == 3:
    program_choice = "Scissors"

print("""Options: 
1. Rock 
2. Paper 
3. Scissors""")

user_number = int(input("Enter your choice (1-3): "))
user_choice = "" 
if user_number == 1:
    user_choice = "Rock"
elif user_number == 2:
    user_choice = "Paper"
elif user_number == 3:
    user_choice = "Scissors"
else: 
    user_choice = "Rock" # defaults to rock 

print("Choices: ")
print(f"Program: {program_choice}")
print(f"User: {user_choice}")

print("Decision: ")
# TODO : Winner implementation (next class)
if program_choice == "Rock" and user_choice == "Paper": 
    print("User is the Winner")
elif program_choice == "Rock" and user_choice == "Scissors": 
    print("Program is the Winner")
elif program_choice == "Paper" and user_choice == "Rock": 
    print("Program is the Winner")
elif program_choice == "Paper"and user_choice == "Scissors": 
    print("User is the Winner")
elif program_choice == "Scissors" and user_choice == "Rock": 
    print("User is the Winner")
elif program_choice == "Scissors" and user_choice == "Paper": 
    print("Program is the Winner")
else: # when they make same choice 
    print("It's a Tie")