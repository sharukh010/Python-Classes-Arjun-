def display(first_name: str,last_name: str)->None: 
    """
    It display first name and last name.

    Args 
    - first_name (str): It is the first name 
    - last_name (str): It is the last name 

    Returns 
    - None 
    - Example: 
    ```
    display("John","Doe")
    ouput: 
    first_name: "John" 
    last_name: "Doe" 
    ```
    """
    print(f"first name: {first_name}")
    print(f"last name: {last_name}")

def add(num1: float,num2: float) -> float: 
    """
    It takes two numbers and returns their sum

    Args
    - num1 (float) 
      It is the first number 
    - num2 (float)
      It is the second number 

    Returns
    - result (float)
      It is the sum of num1 and num2 

    Example
    ```
    add(10,20)
    o/p: 
    30

    add(1.5,2.5)
    o/p: 
    4.0
    ```
    """
    result = num1 + num2 
    return result 

add()
display()