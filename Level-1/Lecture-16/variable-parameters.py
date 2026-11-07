# def addition(*nums): 
#     total = 0 
#     for num in nums: 
#         total += num 

#     return total 

# print(addition(1,2))
# print(addition(1,2,3,4,5,6,7,8,9,10))

# def display(comic_publisher,*characters): 
#     print(f"{comic_publisher}: ")
#     for character in characters: 
#         print(character)
def display(*characters,comic_publisher): 
    print(f"{comic_publisher}: ")
    for character in characters: 
        print(character)

display("Moon knight","Spider man","Thor","Iron Man",comic_publisher="Marvel")
display("Aquaman","Batman","Superman","Black Adam","Shazam",comic_publisher="DC")