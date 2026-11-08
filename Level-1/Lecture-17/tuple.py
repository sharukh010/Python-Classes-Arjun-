directions = ("east","west","north","south")
# print(directions[2])
# you cannot add new elements , you cannot remove existing element , you cannot 
"""
usecase of list: 
1. contacts storage 
2. todos 
3. shopping list 
usecases of tuple: 
1. directions / operations in a game 
"""
# print(*directions) # unpacking tuple same thing we can do with list 
directions_v2 = (*directions,"north east","north west","south east","south west")
# print(directions_v2)
directions.count("east") # this coutns the occurenece of east in our tuple 
directions.index("east") # this gets the index of east 