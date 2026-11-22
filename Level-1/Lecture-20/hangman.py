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
        "difficulty": "easy",
        "hint": "animal",
        "name": "elephant"
    },
    {
        "difficulty": "easy",
        "hint": "food",
        "name": "pizza"
    },
    {
        "difficulty": "easy",
        "hint": "color",
        "name": "purple"
    },
    {
        "difficulty": "medium",
        "hint": "country",
        "name": "japan"
    },
    {
        "difficulty": "medium",
        "hint": "sport",
        "name": "badminton"
    },
    {
        "difficulty": "medium",
        "hint": "technology",
        "name": "robotics"
    },
    {
        "difficulty": "medium",
        "hint": "invention",
        "name": "telescope"
    },
    {
        "difficulty": "hard",
        "hint": "science",
        "name": "astrophysics"
    },
    {
        "difficulty": "hard",
        "hint": "mathematics",
        "name": "trigonometry"
    },
    {
        "difficulty": "hard",
        "hint": "geography",
        "name": "archipelago"
    }
]

word = random.choice(words)
blanks = ["_"for i in range(len(word["name"]))]
blanks_count = len(word["name"])
incorrect = 0 
while True: 
    print("Hangman: ")
    print(hangman[incorrect])
    display(word,blanks)
    if incorrect == len(hangman)-1: 
        print("Game over..")
        break 
    if blanks_count == 0: 
        print("Game over..")
        break 
    character = input("Enter a character: ").lower()
    if character not in word["name"]: 
        incorrect += 1 
    else: 
        count = word["name"].count(character)
        index = -1 
        while count > 0: 
            index = word["name"].index(character,index+1)
            blanks[index] = character
            blanks_count -= 1 
            count -= 1


