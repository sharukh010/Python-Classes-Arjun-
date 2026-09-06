import random 
# generate a random number between 1 3 
program_number = random.randint(1,3)
program_choice = ""
if program_number == 1:
    program_choice = "Rock"
elif program_number == 2:
    program_choice = "Paper"
elif program_number == 3:
    program_number = "Scissors"

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

# TODO : Winner implementation (next class)