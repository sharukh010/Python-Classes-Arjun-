"""
1. we are going to generate 0-1 randomly
2. if it is 0 we say it is head 
else it is tail  
"""
# import statments should be at begining on top 
import random 

number = random.randint(0,1)

if number == 0: 
    print("Heads")
else: 
    print("Tails")