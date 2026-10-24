description = """Version-1:
This application will convert text numbers to actual numbers 
Ex: 
if you enter: "one" it gives 1 
             "two" it gives 2 
- enter the text in lower case 
Note: Currently it only works with single digit"""
print(description)

text = input("Text Number: ")
match text:
    case "zero": 
        print(0) 
    case "one": 
        print(1)
    case "two": 
        print(2)
    case "three":
        print(3)
    case "four":
        print(4)
    case "five": 
        print(5)
    case "six": 
        print(6)
    case "seven": 
        print(7)
    case "eight": 
        print(8)
    case "nine": 
        print(9)
    case _ : 
        print("Nan")