# Functions are used to write reusable code 
# parameters is like the input for a function 

"""
Example to understand functions which take parameters and which don't: 
1) Temperature change button in AC: 
when ever you want to change the temperature we need to provide the temperatrue 
value 
- without temperature value the temperature cannot be changed 
ex: whenever you want to print something you need to pass the value 
- whenever we are dailling someone we need their number without out it we cannot perfrom dailing operation 
- here number is the parameter for dailing function 
2) Power on/off: 
whenever you turn on/off the AC you don't need any input other than the button press 
- volume up / down , whenever you need to up/down the volume you don't need to provide any parameter 


Examples of functions which return some value and which doesn't return any value: 
1) you order a pizza and the app shows pizza is ordered 
- you're just printing the data , but you're not getting any order to you 
- they are not returning any pizza to you 
2) you ordered pizza and the delivery man deliverd the pizza 
- here the are returning the pizza to you 

syntax: 
def function_name(parameters...): 
    logic 
    return value 
"""
# example of function which takes parameters 
# def add(num1,num2): 
#     print(num1+num2) # you dont have full control over the calculated value 

def add(num1,num2): 
    return num1 + num2 
# this is an example of function without parameters
def greet(): 
    print("hello")

# greet()
# (10 + 20) x 3 
print(add(10,20)*3)
# add(10,20)
# add(40,50)
# add(60,70)