word=input("Text: ").lower()
# abc -> abc 
# ABC -> abc 
"""
Explore: 
upper() 
lower() 
captalize() 
ctrl+F2 -> replace all occurence of a word 
"""
morse_code=""
for letter in word:
    match letter: 
        case "a":
            morse_code+=(".-")
        case "b":
            morse_code+=("-...")
        case "c":
            morse_code+=("-.-.")
        case "d":
            morse_code+=("-..")
        case "e":
            morse_code+=(".")
        case "f":
            morse_code+=("..-.")
        case "g":
            morse_code+=("--.")
        case "h":
            morse_code+=("....")
        case "i":
            morse_code+=("..")
        case "j":
            morse_code+=(".---")
        case "k":
            morse_code+=("-.-")
        case "l":
            morse_code+=(".-..")
        case "m":
            morse_code+=("--")
        case "n":
            morse_code+=("-.")
        case "o":
            morse_code+=("---")
        case "p":
            morse_code+=(".--.")
        case "q":
            morse_code+=("--.-")
        case "r":
            morse_code+=(".-.")
        case "s":
            morse_code+=("...")
        case "t":
            morse_code+=("-")
        case "u":
            morse_code+=("..-")
        case "v":
            morse_code+=("...-")
        case "w":
            morse_code+=(".--")
        case "x":
            morse_code+=("-..-")
        case "y":
            morse_code+=("-.--")
        case "z":
            morse_code+=("--..")
        case " ": 
            morse_code += ("/")
        case _:
            morse_code+=("#")
    morse_code += " "
print("Morse Code: ",morse_code)