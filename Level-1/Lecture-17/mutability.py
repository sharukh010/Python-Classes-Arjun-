# mutability - the ability to modify the value inside a container is called mutability 
# immutable - the ability of a container to not modify its values 

# names = ["arjun","arun"]
# # list is mutable 
# print(f"Before making changes: {id(names)}")
# # adding is possible 
# names.append("Bhuvan")
# # removing elements is also possible 
# names.pop()
# #updating is also possible 
# names[0] = "Arjun"
# print(f"After making changes: {id(names)}")

# name = "Ajun" # strings are immutable 
# print(f"Before Updating: {id(name)}")
# # updating is not possible 
# # name[0] = "a"

# # removing element is not possible 
# # name.pop() # It doesn't work 

# name = "Arjun" # this is possible 
# print(f"After Updating: {id(name)}")

# gender = False 
# print(id(gender))
# gender = True 
# print(id(gender))