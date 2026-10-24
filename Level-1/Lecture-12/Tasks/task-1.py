base = int(input("Enter the base value: "))
power = int(input("Enter the power value: "))
result = 1 
count = 0
# count == power i need to stop 
# count != power 
"""
opposite: 
> - < 
< - > 
>= - < 
<= - > 
== - != 
you will only run while loop when the condition is true or else you stop the loop 

base = 2 
power = 3 
count = 0 

count = 1 and power = 3 ; count != power True 
count = 2 and power = 3; count != power True 
count = 3 and power = 3; count != power False <- the loop will stop 
when the while loop is false you will go to line number 28 
""" 
while count != power: 
    result = result * base
    count += 1 

print(result) 