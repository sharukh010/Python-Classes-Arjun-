"""
write a program which takes two numbers as input 
num1 and num2 
and you need to find out how many times num1 can be divided with num2 
ex: 
num1 = 10 
num2 = 2 

10/2 = 5/2 = 2/2 = 1 / 2 = 0 

5/2 = 2.5 
5//2 = 2
"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
count = 0 
while num1 != 0 : 
    num1 = num1 // 2 
    count += 1 

print(f"I'm able to divide {count} times")