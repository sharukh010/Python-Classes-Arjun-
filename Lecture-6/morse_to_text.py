morse_code = input("Morse Code: ")
letter = ""
morse_symbols = morse_code.split()
for morse_symbol in morse_symbols: 
    match morse_symbol:
        case ".-":
            letter += "a"
        case "-...":
            letter += "b"
        case "-.-.":
            letter += "c"
        case "-..":
            letter += "d"
        case ".":
            letter += "e"
        case "..-.":
            letter += "f"
        case "--.":
            letter += "g"
        case "....":
            letter += "h"
        case "..":
            letter += "i"
        case ".---":
            letter += "j"
        case "-.-":
            letter += "k"
        case ".-..":
            letter += "l"
        case "--":
            letter += "m"
        case "-.":
            letter += "n"
        case "---":
            letter += "o"
        case ".--.":
            letter += "p"
        case "--.-":
            letter += "q"
        case ".-.":
            letter += "r"
        case "...":
            letter += "s"
        case "-":
            letter += "t"
        case "..-":
            letter += "u"
        case "...-":
            letter += "v"
        case ".--":
            letter += "w"
        case "-..-":
            letter += "x"
        case "-.--":
            letter += "y"
        case "--..":
            letter += "z"
        case "/":
            letter += " "
        case _:
            letter += "#"
print("Text: ",letter.upper())