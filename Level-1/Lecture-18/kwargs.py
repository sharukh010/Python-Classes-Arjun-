#kwargs -> keyword arguments 
def display(**family): 
    for member in family.items():
        print(f"{member[0].title()}: {member[1].title()}")

# display(me="peter parker",aunt="may parker",uncle="ben parker")
display(me="harry potter",father="xyz",mother="abc",sister="hello")
"""
define function name generate_bill
it take multiple items along with their prices 

sample Input: 
generate_bill(pizza=20,burger=15,coke=10)

sample output: 
Your Order: 
Pizza: $20 
Burger: $15 
Coke: $10 
=============
Total: $45 
"""