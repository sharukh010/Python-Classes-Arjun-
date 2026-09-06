# if (one if)
# elif (many)
# ..... 
# else (one else)
color = input("Enter colour: ")
# if color == "red": 
#     print("Stop")
# elif color == "yellow": 
#     print("Wait")
# elif color == "green": 
#     print("Go")
# else: 
#     print("Invalid color")
# if color == "red": 
#     print("Stop")
# if color == "yellow": 
#     print("Wait")
# if color == "green": 
#     print("Go")
# else: 
#     print("Invalid color")
# if you want to add exclusivity we add a flag (boolean variable)
flag = False # i.e, no condition is satisfied 
if color == "red": 
    print("Stop")
    flag = True 
if color == "yellow" and flag == False: 
    print("Wait")
    flag = True 
if color == "green"  and flag == False: 
    print("Go")
    flag = True 
if flag == False : 
    print("Invalid color")