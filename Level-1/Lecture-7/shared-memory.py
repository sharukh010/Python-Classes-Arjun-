person = "arjun"
friend = "arjun"
class_mate = "arjun"
# print(f"ID of Person: {id(person)}")
# print(f"ID of Friend: {id(friend)}")
# print(f"ID of Class mate: {id(class_mate)}")
# in heap memory before store a date 
# first you will check if it is already present in the heap memory or not 
# if you already have the value multiple variables point to same location 
# because of the immutability of heap memory when ever you update a variable value it will not effect the shared memory 
class_mate = "arun"
print(f"ID of Person: {id(person)}")
print(f"ID of Friend: {id(friend)}")
print(f"ID of Class mate: {id(class_mate)}")