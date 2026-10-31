products = [
    "IPhone Duo",
    "Macbook",
    "Chair",
    "Pencils",
    "Pens"
]

cart = [] 
orders = [] 


def display_products(): 
    print("Products: ")
    for i in range(len(products)): 
        print(f"{i+1}. {products[i]}")

def display_orders(): 
    print("Orders: ")
    if len(orders) == 0: 
        print("No orders")
    else: 
        for pid in orders: 
            print(f"{pid+1}. {products[pid]}")

def display_cart(): 
    print("Cart: ")
    if len(cart) == 0: 
        print("Cart is empty...")
    else: 
        for pid in cart: 
            print(f"{pid+1}. {products[pid]}")

options = """Options: 
1. Add to Cart 
2. Cart Checkout
3. Display orders
4. Display cart
5. Exit"""
while True: 
    print("Pymart: ")
    print(options)
    choice = int(input("Enter your choice (1-4): "))
    match choice: 
        case 1: 
            display_products()
            pid = int(input("Enter product ID: "))
            if pid <= 0 or pid > len(products): 
                print("Invalid Product ID. Try again")
            else: 
                cart.append(pid-1)
                print("Successfully added to cart")
        case 2: 
            orders.extend(cart)
            cart.clear() 
            print("Successfully Purchased all the products")
        case 3: 
            display_orders() 
        case 4: 
            display_cart()
        case 5: 
            print("Exiting...")
            break 
        case _: 
            print("Invalid choice. Try again")
    print("="*20)