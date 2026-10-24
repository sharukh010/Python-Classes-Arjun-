def display(first_name: str,last_name: str)->None: 
    print(f"first name: {first_name}")
    print(f"last name: {last_name}")


# display("John","Doe") # positional arguments 
# display("Doe","John")
# display("John") # we cannot do this 

# display(first_name="John",last_name="Doe")
display(last_name="Doe",first_name="John")
# keyword argument 