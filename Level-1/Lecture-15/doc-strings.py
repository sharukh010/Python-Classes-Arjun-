def add(a: int | float ,b: int | float ) -> int | float : 
    """
    It take two numbers and returns the sum

    Args
    - a (int | float) : first number 
    - b (int | float) : second number 

    Returns
    - a + b (int | float) : sum of the two number

    Ex
    ```
    add(1,2) -> returns 3 
    add(2.5,1.5) -> returns 4.0
    ```
    """
    return a + b 
# parameter: data type (int,float,str,bool)
def sum(nums: list[int | float]) -> int | float :
    """
    It takes a list of numbers and return their sum

    Args
    - nums (list[int | float]): list of the numbers 

    Returns 
    - total (int | float): sum of all the numbers
    
    Example
    ```
    nums = [1,2,3,4,5]
    total = sum(nums)
    print(total)
    ```
    Output
    ```
    15
    ```
    """
    total = 0 
    for i in nums: 
        total += i 
    return total 

# add(1,2)
sum()