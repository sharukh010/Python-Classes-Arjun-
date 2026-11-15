#kwargs -> keyword arguments 
def display(**family): 
    for member in family.items():
        print(f"{member[0].title()}: {member[1].title()}")

# display(me="peter parker",aunt="may parker",uncle="ben parker")
display(me="harry potter",father="xyz",mother="abc",sister="hello")