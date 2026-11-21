"""
Project 7: MCQ Quiz Game (Group 7)
Topic: Python Basics
Members: Ashish Gupta,Vivek Yadav, Shubham Kumar, Aditya Maurya
Features:
- 12 questions, each stored as a tuple: (question, (4 options), correct_option_number)
- All questions held in a dictionary
- Questions asked in random order using random.shuffle
- +1 for a correct answer, negative marking for a wrong one
- Final score with a grade
- Leaderboard saved in a file
- used:- Python basics, Nested loops, Sets, Tuples, Dictionaries, File Handling,
- Functions, Random module, String methods, Input validation

Run the quiz:      python quiz.py
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


def get_grade(score, total):
    """Return a grade based on the percentage."""
    if total == 0:
        return "F"
    
    percent = score / total * 100
    if percent >= 90:
        return "A+"
    elif percent >= 75:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 40:
        return "C"
    else:
        return "F"


def get_answer():
    """Keep asking until the player types 1, 2, 3 or 4."""
    answer = input("Your answer (1-4): ")
    # isdigit() checks that the text is a number, so we don't need try/except
    while not answer.isdigit() or int(answer) < 1 or int(answer) > 4:
        print("  Please type a number between 1 and 4.")
        answer = input("Your answer (1-4): ")
    return int(answer)


def save_score(name, score, total, grade):
    """Append the result to the leaderboard file (mode 'a' = append)."""
    file = open(LEADERBOARD_FILE, "a")
    file.write(name + "," + str(score) + "," + str(total) + "," + grade + "\n")
    file.close()


def show_leaderboard():
    """Read the leaderboard file (mode 'r') and print the top 5 scores."""
    # Make sure the file exists. Mode 'a' creates it if it is missing.
    file = open(LEADERBOARD_FILE, "a")
    file.close()

    file = open(LEADERBOARD_FILE, "r")
    lines = file.readlines()
    file.close()

    # Put every line into a list of [score, name, total, grade]
    entries = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:          # only use lines in the correct format
            name = parts[0]
            score = float(parts[1])
            total = parts[2]
            grade = parts[3]
            entries.append([score, name, total, grade])

    # Sort so the highest score comes first
    entries.sort(reverse=True)

    print("\n====== LEADERBOARD (Top 5) ======")
    rank = 1
    for entry in entries:
        if rank > 5:
            break
        print(rank, "-", entry[1], "-", entry[0], "/", entry[2], "-", entry[3])
        rank = rank + 1


def main():
    print("=== MCQ Quiz Game: Python Basics ===")
    name = input("Enter your name: ")
    name = name.replace(",", "").strip()  # a comma would break our file format
    if name == "":
        name = "Player"

    print("\nHello,", name + "!")
    print("Correct answer = +1 mark, wrong answer = -0.25 mark.")
    print("Let's start!\n")

    # Shuffle the question numbers to get a random order
    order = list(QUIZ.keys())
    random.shuffle(order)

    score = 0
    position = 1

    # A normal for loop 
    for q_no in order:
        question = QUIZ[q_no][0]
        options = QUIZ[q_no][1]
        correct = QUIZ[q_no][2]

        print("\nQuestion", position, "of", len(order))
        print(question)

        # Print the 4 options
        number = 1
        for option in options:
            print(" ", number, ".", option)
            number = number + 1

        choice = get_answer()

        if choice == correct:
            print("  Correct! +1")
            score = score + 1
        else:
            print("  Wrong! The correct answer is", correct, "(-0.25)")
            score = score - NEGATIVE_MARK

        position = position + 1

    total = len(QUIZ)
    grade = get_grade(score, total)

    print("\n========== RESULT ==========")
    print("Final score:", score, "/", total)
    print("Grade:", grade)

    save_score(name, score, total, grade)
    show_leaderboard()


main()
