description = """Version-1:
This application will convert text numbers to actual numbers 
Ex: 
if you enter: "one two three" it gives 123 
             "two one two" it gives 212 
- enter the text in lower case 
Note: Nan means the program is unable to find the number for the word"""
print(description)
"""
when ever you use print function after printing it will move to next line 
because by default print end parameter is set to '\n' new line character
"""
text = input("Text Number: ")
for text_number in text.split(): 
    match text_number:
        case "zero": 
            print(0,end="") 
        case "one": 
            print(1,end="")
        case "two": 
            print(2,end="")
        case "three":
            print(3,end="")
        case "four":
            print(4,end="")
        case "five": 
            print(5,end="")
        case "six": 
            print(6,end="")
        case "seven": 
            print(7,end="")
        case "eight": 
            print(8,end="")
        case "nine": 
            print(9,end="")
        case _ : 
            print("Nan",end="")