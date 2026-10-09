# Week 07 Assignment: Gradebook Function Suite

## What You Are Building

Build a small gradebook helper program. Your program should use functions to calculate and summarize student scores stored in collections.

Example idea: a teacher has student names, assignment scores, and a few missing submissions. Your functions should help calculate averages, find the highest score, decide whether a student is passing, and print a clear report.

## Textbook And Reference Sections

- Official textbook: Chapter 6, Fruitful functions
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html>
- Useful review: Chapter 11, Lists
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/lists.html>
- Additional reference: <https://www.w3schools.com/python/python_functions.asp>

## Concepts You Need

- Fruitful functions use `return` to send an answer back.
- A function should do one clear job.
- Lists can store multiple scores in order.
- Dictionaries can connect a name to that student's scores.
- Simple tests prove a function before it is used in a larger program.
- A demo section combines collections, conditionals, loops, and function calls.

## Small Example

```python
def average(scores):
    return sum(scores) / len(scores)


gradebook = {
    "Maya": [9, 10, 8],
    "Noor": [7, 8, 9],
}

print("Maya average:", average(gradebook["Maya"]))
```

## Requirements I Will Check

- [ ] Create a dictionary named `gradebook` where each key is a student name and each value is a list of scores.
- [ ] Write at least four functions.
- [ ] Include a function named `average(scores)` that returns the average of a list of scores.
- [ ] Include a function named `student_average(gradebook, name)` that returns one student's average.
- [ ] Include a function named `is_passing(average_score)` that returns `True` or `False`.
- [ ] Include a function named `print_report(gradebook)` that loops through the dictionary and prints each student's average and passing status.
- [ ] Use at least one list loop and at least one dictionary loop.
- [ ] Use a clear demo section that calls every function.
- [ ] Include at least four test calls with expected results in comments or printed labels before the final report.
- [ ] Use meaningful function and variable names.
- [ ] Avoid repeated calculation code by calling functions instead.
- [ ] `notes.md` explains which function was hardest to test and why.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Function correctness | 4 | Functions return correct gradebook results for normal inputs |
| Testing | 2 | Expected outputs are shown or explained |
| Integration | 2 | Demo calls every function and prints a complete report |
| Code quality | 2 | Names and structure make the program readable |

## Stretch 1

- [ ] Add a function named `lowest_student_average(gradebook)` that returns the name and average of the student with the lowest average.
- [ ] Add a function named `class_average(gradebook)` that returns the average score across all students and all assignments.
- [ ] Add two more tests that prove these functions work.

## Stretch 2

- [ ] Track missing work with a set named `missing_work`.
- [ ] Add a function named `needs_follow_up(name, average_score, missing_work)` that returns `True` when a student is not passing or has missing work.
- [ ] Update the report so it clearly marks students who need follow-up.
- [ ] Include one function that calls at least two other functions.

## Submission Checklist

- [ ] Branch name is exactly `week-07-function-suite`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
