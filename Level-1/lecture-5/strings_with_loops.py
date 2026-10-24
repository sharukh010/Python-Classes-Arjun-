# directly accessing them using for loop 
name = "Arjun"
#   varaible     sequence name 
# for character in name: 
#     print(character)

# using indexes 
# index this are positions , how many characters you need to skip to reach their 
"""
A r j u n 
0 1 2 3 4 
"""
# print(name[0])
length = len(name) # this will give you the length of the string 
for index in range(length): # 0 1 2 3 4 
    print(name[index]) 
