def calculate_bill(customer_name,pizza_size="Medium",*toppings): 
    total_price = 0 
    base_price = 0 
    match pizza_size: 
        case "Small": 
            base_price = 150 
        case "Medium": 
            base_price = 250 
        case "Large": 
            base_price = 350 
    number_of_toppings = len(toppings)
    toppings_price = number_of_toppings * 30 
    total_price += toppings_price + base_price
    discount = 0 
    if pizza_size == "Large" and number_of_toppings > 3:
        discount = (10/100) * total_price  
        total_price = total_price - discount 

    bill = f"""
    Customer Name: {customer_name}
    Pizza Size: {pizza_size}
    Toppings: {toppings}
    Base Price: ₹{base_price}
    Toppings Cost: ₹{toppings_price}
    Discount: ₹{discount}
    Final Bill: ₹{total_price}

    """
    print(bill)

calculate_bill("Ryan", "Large", "Cheese", "Olives", "Mushrooms", "Corn")
