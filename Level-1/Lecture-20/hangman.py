import random 
def display(word: dict,blanks: list): 
    print(f"Difficulty: {word["difficulty"]}")
    print(f"Hint: {word["hint"]}")
    print(f"Name: {" ".join(blanks)}")
hangman = [

"""






===
""",
"""
 |
 |
 |
 |
 |
 |
===
""",
"""
 |===========
 |
 |
 |
 |
 |
===
""",
"""
 |===========
 |          |
 |
 |
 |
 |
===
""",
"""
 |===========
 |          |
 |          O
 |
 |
 |
===
""",
"""
 |===========
 |          |
 |          O
 |          |
 |
 |
===
""",
"""
 |===========
 |          |
 |          O
 |         /|
 |
 |
===
""",
"""
 |===========
 |          |
 |          O
 |         /|\\
 |
 |
===
""",
"""
 |===========
 |          |
 |          O
 |         /|\\
 |         /
 |
===
""",
"""
 |===========
 |          |
 |          O
 |         /|\\
 |         / \\
 |
===
"""

]

words = [
    {
        "difficulty":"easy",
        "hint":"fruit",
        "name":"mango"
    },
    {
        "difficulty":"medium",
        "hint":"place",
        "name":"chicago"
    },
    {
        "difficulty":"hard",
        "hint":"subject",
        "name":"thermodynamics"
    }
]

word = random.choice(words)
blanks = ["_"for i in range(len(word["name"]))]
incorrect = 0 
while True: 
    print("Hangman: ")
    print(hangman[incorrect])
    if incorrect == len(hangman)-1: 
        print("Game over..")
        break 
    display(word,blanks)
    character = input("Enter a character: ").lower()
    if character not in word["name"]: 
        incorrect += 1 

