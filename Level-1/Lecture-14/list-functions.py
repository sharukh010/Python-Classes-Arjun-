ages = [12,3,45,77,28,77]
# len -> it is to find the length of the list 
# print(len(ages))

# copy -> it is to create copy of the list 
# ages_copy = ages.copy()
# print(f"Original list: {ages}")
# print(f"Copy list: {ages_copy}")

# index -> this takes the value and returns the index of the value in the list (first occurence)
# print(f"Index of 77: {ages.index(77)}")

# count -> this will take the value and return the count of value in the list 
# print(f"Count of 77: {ages.count(77)}")

# reverse -> reverse the order of the list 
# ages.reverse()
# print(f"Reverse: {ages}")

# sort 
# ages.sort()
# ages.sort(reverse=True)
# print(f"Sorted: {ages}")

# append - this is used to add an element at the end of the list 
# ages.append(100)
# print(ages)

# extend - it takes another list as input and adds it at the end of current list 
# this is like append which can add multiple values 

ages.extend([1,2,3,4,5])
print(ages)