ages = [12,13,25,32]
# print(ages) # o/p: [12,13,14,15]
# print(ages[2]) # o/p: 25 
# print(ages[-1])#32
# print(len(ages))
# print(sum(ages))
# print(max(ages))
# print(min(ages))
# accessing elements one by one with using indexes and loop 
# length = len(ages)
# for index in range(length): 
#     print(ages[index])
# accessing elements one by one without using indexes 
# for age in ages:
#     print(age) 
# using list slicing you can access multiple elements 
# print(ages[1:3])
# print(ages[:4])# start = 0 
# print(ages[1:])# end = 5  
# print(ages[:])
# print(ages[::2])# step will tell you what to add to current index to get the next element index
print(ages[::-1])