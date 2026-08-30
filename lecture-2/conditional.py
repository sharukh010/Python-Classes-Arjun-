"""
A number as input and we are going to say 
if it is even number or odd number. 
Algorithm: (sequence of steps written in plain english text)
1. take the number as input from the  user 
2. check if it is even 
 - if yes we will print even 
 - if no we will print odd 

algorithms -> write the code in any programming language
syntax -> grammar of programming language 
ex: 
1. my name is sharukh (correct) (it is correct grammar)
2. name my is sharukh (wrong) its wrong grammar (syntax)

variable = value (correct)
value = variable (not correct) not following python syntax

syntax of if statment: 
if condition: <- : specify that after this a new code block 
is going to start i.e there are bunch of lines that comes under 
if condition 
after : we can have code inside if condition and 
code outside if condition 
so to differentiate we use indentation (spaces before lines)
    line -1 (belong to if)
    line -2 (belong to if)
    line -3 (belong to if)
line - 4 (doesn't belong to if)

to understand how to write conditions we need to learn 
about comparision operators 
"""
number = int(input("Enter a number: ")) # taking number as input 
if number %2 == 0: 
    print("It is even")
else: 
    print("It is odd")