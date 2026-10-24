"""
Write a program which takes numbers from a user. The user will give the numbers one by one. You should stop taking the numbers as input whenever the user gives you 0 as the input. Once you receive the 0, you need to find the sum of all the numbers that were given until now, and you need to print the sum. 
"""
# num = -1
# total = 0 
# while num != 0 : 
#     num = int(input("Enter the number: "))
#     total += num 
# print(f"Total: {total}")
# infinite loop 
# while True: # while 1 < 2 
#     print("hello")
total = 0 
while True: 
    num = int(input("Enter the number: "))
    if num != 0: 
        total = total + num 
    else: 
        break # this will stop the loop 
print(f"total: {total}")