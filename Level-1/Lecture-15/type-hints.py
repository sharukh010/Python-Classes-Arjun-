def add(a: int | float ,b: int | float ) -> int | float : 
    return a + b 
# parameter: data type (int,float,str,bool)
def sum(nums: list[int | float]) -> int | float : 
    total = 0 
    for i in nums: 
        total += i 
    return total 

print(add("trida",10))