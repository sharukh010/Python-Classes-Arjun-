# name = "arjun"
# print(f"Arjun ID: {id(name)}")
# # string is immutable 
# # print(name[2])
# # name[2] = "" this will not happen 
# name = "arun"
# print(f"Arun ID: {id(name)}")

nums = [10,20,30] # mutable 
print(f"Nums ID: {id(nums)}")
nums[2] = 40 
print(f"Nums ID: {id(nums)}")