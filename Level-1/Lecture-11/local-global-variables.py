def demo(): 
    global name 
    # local variable 
    nums = 10 
    name = "bob"
    # when you do this function will think that 
    # you're updating a local variable 
    print("Inside function: ",nums)
    print("Inside function: ",name)

nums = 20 # global 
name = "arjun"
demo()
# name = "kevin"
# demo()
print("Outside function: ",name)
print("Outside function: ",nums)