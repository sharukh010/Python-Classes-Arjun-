dummy = {"a":1,"b":2,"c":3}
"""
keys: a,b,c
values: 1,2,3
"""
# print(dummy.keys()) # keys -> will give list of all the keys in dict 
# print(dummy.values())# values -> will give list of all the values in dict
# print(dummy.items())#items -> will give list of (key,value) tuple

# print(dummy.get("d",0)) # get -> it will get the value if it is there in the dictionary or else it will return default value (None)

# print(dummy.copy()) # copy -> creates a copy of given dictionary 

# dummy.clear() # clear -> will clear all the key-value pairs in dict 
# del dummy["a"] # del -> deletes the data from memory 
# print(dummy)


# value = dummy.pop("a") # pop takes a key  and return the value and then delete it form dictionary 
# print(value,dummy)

# fromkeys -> it is used to create a dictionary from fixed set of keys and a default value 
# person = dict.fromkeys(["name","age","gender","city","hobbies"],None)
# print(person)


# dummy.update({"a":10,"d":20}) # updates values of exisiting keys and adds new key value paris 
# print(dummy)

# value = dummy.setdefault("d",4)# it is combination of get and update 
# # if there is a key it will get the value if there is no key it will add it to the dictionary
# print(value,dummy)

# print(dummy.popitem()) # removes the last key value pair as a tuple 

# print(len(dummy))

# print("a" in dummy) # we can use membership operators to check for keys 
print(1 in dummy.values())