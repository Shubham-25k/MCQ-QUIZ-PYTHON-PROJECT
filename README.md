# 🧠 MCQ Quiz Game — Python Basics

A command-line multiple-choice quiz written in pure Python. Answer 12 questions on Python basics, get scored with **negative marking**, receive a **grade**, and see how you rank on a file-based **leaderboard**.

> **Course Project 7 · Group 7** — Python Programming (First Year B.Tech)

---

## ✨ Features

- 📚 **12 questions** on Python basics, each stored as a tuple: `(question, (4 options), correct_option_number)`
- 🗂️ All questions held in a single **dictionary** (`QUIZ`)
- 🔀 Questions asked in a **random order** every game using `random.shuffle`
- ➕ **+1** for a correct answer, ➖ **−0.25** for a wrong answer
- 🏅 Final score with a **grade** (A+, A, B, C or F)
- 🏆 **Leaderboard** saved in `leaderboard.txt` — top 5 scores shown after every game
- 🛡️ **Input validation** — letters, symbols or numbers outside 1–4 are rejected and the question is asked again

---

## 🎮 How to Play

1. Enter your name.
2. Read each question and its four options.
3. Type the option number (**1–4**) and press **Enter**.
4. After the last question you will see your final score, grade and the Top 5 leaderboard.

### Sample output

```text
=== MCQ Quiz Game: Python Basics ===
Enter your name: Vivek

Hello, Vivek!
Marks awarded for Correct answer = +1 mark,marks deducted for wrong answer = -0.25 mark.

Question 1 of 12
Which of these data types is immutable?
  1 . list
  2 . dict
  3 . tuple
  4 . set
Your answer (1-4): abc
  Please type a number between 1 and 4.
Your answer (1-4): 3
  Correct! +1

...

========== RESULT ==========
Final score: 8.25 / 12
Grade: B

====== LEADERBOARD (Top 5) ======
1 - Vivek - 8.25 / 12 - B
2 - Ashish - 5.75 / 12 - C
```

---

## 📊 Scoring & Grading

| Answer  | Marks  |
|---------|--------|
| Correct | +1     |
| Wrong   | −0.25  |

Maximum score is **12**, minimum is **−3**. Grade is based on `percentage = score ÷ total × 100`:

| Percentage         | Grade |
|--------------------|-------|
| 90 and above       | A+    |
| 75 to less than 90 | A     |
| 60 to less than 75 | B     |
| 40 to less than 60 | C     |
| Below 40           | F     |

---

## 🏆 Leaderboard

Every result is appended to `leaderboard.txt` as one comma-separated line:

```text
name,score,total,grade
Ashish,5.75,12,C
```

- The file is created automatically if it does not exist.
- Entries are sorted so the highest score comes first; the top 5 are displayed.
- Commas are removed from player names so they cannot break the file format.

---

## 🗂️ Project Structure

```text
.
├── quiz.py            # Main program (the whole game)
├── leaderboard.txt    # Saved scores (auto-updated after each game)
└── README.md          # You are here
```

### Functions in `quiz.py`

| Function                                | What it does                                                        |
|-----------------------------------------|---------------------------------------------------------------------|
| `get_answer()`                          | Keeps asking until the player types 1, 2, 3 or 4                    |
| `get_grade(score, total)`               | Converts the score into a percentage and returns the grade          |
| `save_score(name, score, total, grade)` | Appends the result to the leaderboard file                          |
| `show_leaderboard()`                    | Reads the file, sorts the scores and prints the top 5               |
| `main()`                                | Runs the whole game: name, shuffle, questions, score, result, board |

---

## 🧩 Python Concepts Used

Strings · Operators · Lists · Tuples · Dictionaries · `if-elif-else` · `for` and `while` loops · **Nested loops** (questions → options) · Functions · `random` module · Input validation · **File handling** (append and read modes)

---

## 🔮 Future Improvements

- Main menu with several rounds and an Exit option
- Recursive question flow and a set to track already-asked questions
- `try-except` error handling and `doctest` examples
- Load questions from an external file; add more topics and difficulty levels
- Timer for each question and a one-entry-per-player leaderboard
- GUI version using Tkinter

---

## 👥 Team — Group 7

| Name          |
|---------------|
| Vivek Yadav   |
| Shubham Kumar |
| Aditya Maurya |
| Ashish Gupta  |

---
