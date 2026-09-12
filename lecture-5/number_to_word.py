number = input("Number: ")
word = ""

for digit in number: 
    match digit: 
        case "0": 
           # word = word + "zero"
           word += "zero"
        case "1": 
           word += "one"
        case "2": 
           word += "two"
        case "3": 
           word += "three"
        case "4": 
           word += "four"
        case "5":
           word += "five"
        case "6": 
           word += "six"
        case "7": 
           word += "seven"
        case "8": 
           word += "eight"
        case "9": 
           word += "nine"
        case _ : 
           word += "nan"
    word += " "
print(word.title())