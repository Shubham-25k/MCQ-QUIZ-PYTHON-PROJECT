"""
Project 7: MCQ Quiz Game (Group 7)
Topic: Python Basics
Members: Ashish Gupta,Vivek Yadav, Shubham Kumar, Aditya Maurya
Features:
- 12 questions, each stored as a tuple: (question, (4 options), correct_option_number)
- All questions held in a dictionary
- Questions asked in random order using random.shuffle
- +1 for a correct answer, negative marking for a wrong one(-0.25)
- Final score with a grade
- Leaderboard saved in a file
- Topics used:- Python basics, Nested loops, Sets, Tuples, Dictionaries, File Handling,
- Functions, Random module, String methods, Input validation
"""

import random

LEADERBOARD_FILE = "leaderboard.txt"
NEGATIVE_MARK = 0.25

# Each question is a tuple: (question, (4 options), correct option number)
# All questions are stored in a dictionary
QUIZ = {
    1: ("Which keyword is used to define a function in Python?",
        ("function", "def", "define", "fun"), 2),
    2: ("What is the output of len('Python')?",
        ("5", "6", "7", "Error"), 2),
    3: ("Which of these data types is immutable?",
        ("list", "dict", "tuple", "set"), 3),
    4: ("What is the value of 2 ** 3?",
        ("6", "8", "9", "5"), 2),
    5: ("Which module provides the shuffle function?",
        ("math", "os", "random", "sys"), 3),
    6: ("Which symbol starts a single-line comment in Python?",
        ("//", "#", "/*", "--"), 2),
    7: ("What does 7 // 2 evaluate to?",
        ("3.5", "3", "4", "2"), 2),
    8: ("Which expression creates an empty set?",
        ("{}", "[]", "set()", "()"), 3),
    9: ("Which list method adds an item at the end?",
        ("add", "append", "insert_end", "push"), 2),
    10: ("Which statement is used to handle exceptions?",
         ("try-except", "catch-throw", "do-catch", "error-handle"), 1),
    11: ("What is the type of 3.0 in Python?",
         ("int", "float", "double", "decimal"), 2),
    12: ("Which file mode opens a file for appending?",
         ("r", "w", "a", "x"), 3),
}

def get_answer():
    """Keep asking until the player types 1, 2, 3 or 4."""
    answer = input("Your answer (1-4): ")
    # isdigit() checks that the text is a number, so we don't need try/except
    while not answer.isdigit() or int(answer) < 1 or int(answer) > 4:
        print("  Please type a number between 1 and 4.")
        answer = input("Your answer (1-4): ")
    return int(answer)

