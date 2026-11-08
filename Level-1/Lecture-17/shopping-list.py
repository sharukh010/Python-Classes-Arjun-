"""
categories: 
1. Grocery
2. Electronic
3. Clothing
4. Toy
5. Cleaning
"""
def display_category(): 
    print("Category: ")
    for i in range(len(category)): 
        print(f"{i+1}. {category[i]}")

def display_items(): 
    print("Shopping List: ")
    for item in items: 
        print(f"{item[0]} - {item[1]}")
category = ("Grocery","Electronic","Clothing","Toy","Cleaning")
items = [] 
options = """Options: 
1. Add an Item 
2. View all the Items 
3. Exit"""
while True:
    print("Shopping List Tracker: ") 
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
            print("Adding an Item: ")
            name = input("Name: ")
            display_category()
            cat = int(input("Enter your choice(1-5): "))
            cat = category[cat-1]
            items.append((name,cat))
            print("Successfully added an item")
        case 2:
            display_items() 
        case 3: 
            print("Exiting..")
            break 