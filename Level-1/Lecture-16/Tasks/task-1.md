## Python Practice Question: Smart Pizza Order System 🍕

### Concepts to Practice

- Default parameters
- Variable-length positional parameters (`*args`)
- Conditional statements
- Functions

### Problem Statement

Create a Python program for a pizza shop called Pizza Planet.

The shop allows customers to order pizzas with different toppings. Your task is to create a function that calculates the total cost of a pizza order.

### Requirements

Create a function named `calculate_bill()` with the following parameters:

```
def calculate_bill(customer_name, pizza_size="Medium", *toppings):
    pass
```

Your function should:

1. Accept the customer's name.
2. Use `"Medium"` as the default pizza size.
3. Accept any number of toppings using variable parameters.
4. Calculate the pizza price based on its size:
   - Small: ₹150
   - Medium: ₹250
   - Large: ₹350
5. Each topping costs ₹30.
6. If the customer orders a Large pizza with more than 3 toppings, provide a 10% discount on the total bill.
7. Display the customer's name, pizza size, toppings, and final bill.
8. If no toppings are provided, display `"No extra toppings"`.

### Sample Function Calls

```
calculate_bill("Alex")
calculate_bill("Emma", "Small", "Cheese", "Olives")
calculate_bill("Ryan", "Large", "Cheese", "Olives", "Mushrooms", "Corn")
calculate_bill("Sophia", "Medium", "Paneer", "Jalapenos", "Onions")
```

### Expected Output (Example)

For the following function call:

```
calculate_bill("Ryan", "Large", "Cheese", "Olives", "Mushrooms", "Corn")
```

The output should look something like this:

```
Customer Name: Ryan
Pizza Size: Large
Toppings: Cheese, Olives, Mushrooms, Corn
Base Price: ₹350
Toppings Cost: ₹120
Discount: ₹47
Final Bill: ₹423
```

### Challenge Questions

1. What happens if the customer provides only the name?
2. What happens if the customer provides 5 toppings?
3. Can you modify the function to accept a default pizza size of `"Small"`?
4. What happens if the customer enters an invalid pizza size?
5. Can you add a new parameter `delivery_charge=40` and include it in the final bill?

Important: Try solving the problem without using lists to collect the toppings manually. Use `*args` to handle them.