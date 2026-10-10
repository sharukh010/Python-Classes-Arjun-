# functions are used for reusability 
# functions are piece of code that has a lable (function name) which you can use to call it whenever you want 
# you should not take input from the user inside a function 
# add two numbers 
# this is wrong way of defining functions 
"""
Reasons: 
1) this function is dependent on user input 
- it cannot be used for any other usecases like trying find addition while writing a program 
2) you need to detach the input logic from the function 

ex: mul(10,20) + mul(1,2) i cannot use it in this case 
"""
# def add(): 
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(num1+num2)
# parameters is the way you can pass input to the data 
def add(num1,num2): 
    result = num1 + num2 
    return result 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
result = add(num1,num2)
print(result)