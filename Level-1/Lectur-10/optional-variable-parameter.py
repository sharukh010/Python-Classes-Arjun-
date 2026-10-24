# you can add optional parameters to a function by providing default values 
# def add(num1: float,num2: float = 0 )-> float: 
#     return num1 + num2 


def add(num1,num2,*nums): 
    result = num1 + num2 
    for num in nums: 
        result += num 

    return result 


# print(add(1))
print(add(1,2,3))
print(add(1,2,3,4,5))