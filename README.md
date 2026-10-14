# IEEE LGU AI/ML Cohort One — Week 1 Assignment

**Name:** Huba Sardar  
**Track:** Artificial Intelligence & Machine Learning  
**Week:** 1 — Python Fundamentals

## Projects Completed

For Week 1, I selected these two projects:

1. **Number Guessing Game**
2. **Student Grade & Attendance Tracker**

Both projects are written in pure Python and use only standard Python features and the built-in `random` module where required.

---

## 1. Number Guessing Game

### Description
The computer randomly selects a number between 1 and 100. The player has 7 attempts to guess the number. The program gives a "Too High" or "Too Low" clue after an incorrect guess, displays remaining attempts, handles invalid input, reveals the secret number if the player loses, and allows the player to play another round.

### Concepts Used
- Variables and data types
- `if`, `elif`, and `else`
- `for` and `while` loops
- Functions
- User input and error handling
- `random.randint()`

### How to Run

```bash
python task1_number_guessing/number_guessing.py
```

---

## 2. Student Grade & Attendance Tracker

### Description
This program collects a student's name and roll number, stores marks for at least three subjects in a dictionary, calculates the average percentage, assigns a letter grade, calculates attendance, and checks whether the student meets the 75% minimum attendance requirement. It then displays a clean report card.

### Grade Rules
- 80% and above → Grade A
- 70% to 79% → Grade B
- 50% to 69% → Grade C
- Below 50% → Grade F

### Concepts Used
- Lists/dictionaries
- Functions
- Loops
- Conditions
- User input
- `try/except` error handling
- Percentage and average calculations

### How to Run

```bash
python task2_student_tracker/student_tracker.py
```

---

## Screenshots

The `screenshots` folder contains terminal-output screenshots demonstrating successful runs and invalid-input handling for both projects.

- `task1_output.png` — Number Guessing Game
- `task2_output.png` — Student Grade & Attendance Tracker

## Repository Structure

```text
ieee-lgu-aiml-week1-Huba-Sardar/
│
├── README.md
├── screenshots/
│   ├── task1_output.png
│   └── task2_output.png
│
├── task1_number_guessing/
│   └── number_guessing.py
│
└── task2_student_tracker/
    └── student_tracker.py
```

## Requirements

- Python 3.8 or newer
- No third-party libraries are required
