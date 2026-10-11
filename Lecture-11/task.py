def multiplier(num): 
    global number 
    number = number * num 

def prefixer(prefix): 
    global text 
    text = f"{prefix} "+text 

number = 10 
text = "arjun"
multiplier(2)
print(number)
prefixer("hero")
print(text)