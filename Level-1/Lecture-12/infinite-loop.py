"""
write a program which greets users with their names 
and stops whenever you enter stop 
"""
while True:
    name = input("Name: ")
    if name == "stop": 
        break 
    else: 
        print(f"Hi, {name}")