numerical_word = input("Word: ")
words = numerical_word.split()
number = ""
"""
i/p: 
one two three -> ("one","two","three")
"""

for word in words: 
    match word: 
        case "one": 
            number += ("1")
        case "two": 
            number += ("2")
        case "three": 
            number += ("3")
        case "four": 
            number += ("4")
        case "five": 
            number += ("5")
        case "six":
            number += ("6")
        case "seven": 
            number += ("7")
        case "eight": 
            number += ("8")
        case "nine": 
            number += ("9")
        case "zero": 
            number += ("0")
print(number)