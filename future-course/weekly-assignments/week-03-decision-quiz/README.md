# Week 03 Future Assignment: Decision Quiz

## What You Are Building

Create a short interactive quiz, recommendation tool, or branching prompt that uses conditionals to make decisions from user input.

## Textbook And Reference Sections

- Official textbook: Chapter 5, Conditionals
- Textbook link: <https://openbookproject.net/thinkcs/python/english3e/conditionals.html>
- W3Schools references:
  - Python Conditions: <https://www.w3schools.com/python/python_conditions.asp>
  - Python Operators: <https://www.w3schools.com/python/python_operators.asp>

## Concepts You Need

- A Boolean expression is either `True` or `False`.
- `if`, `elif`, and `else` let a program choose between paths.
- `==` compares values. `=` assigns a value.
- `and`, `or`, and `not` combine or reverse conditions.
- `.strip()` and `.lower()` can clean text input before comparison.

## Small Example

```python
answer = input("Do you like Python? ").strip().lower()
if answer == "yes":
    print("Excellent choice.")
else:
    print("Keep practicing.")
```

## Requirements I Will Check

- [ ] Ask the user at least three questions with `input()`.
- [ ] Use `.strip()` or `.lower()` on at least one text input before comparing it.
- [ ] Use at least one equality comparison with `==`.
- [ ] Use at least one inequality comparison with `!=`, `<`, `<=`, `>`, or `>=`.
- [ ] Use at least one `if` / `else` decision.
- [ ] Use at least one `if` / `elif` / `else` chain with three or more paths.
- [ ] Use at least one multiple-condition expression with `and` or `or`.
- [ ] Track a score, category, or result variable.
- [ ] Print a final result that depends on that variable.
- [ ] `notes.md` includes at least three test cases showing different paths.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Conditional logic | 4 | Required comparison and branching forms appear correctly |
| Input cleanup | 2 | Uses `.strip()` or `.lower()` appropriately |
| Result tracking | 2 | Score/category/result changes based on answers |
| Testing | 2 | Tests show different paths |

## Stretch 1

- [ ] Add validation for at least one invalid answer.
- [ ] Use both `and` and `or`.
- [ ] Add two more tests for validation or combined conditions.

## Stretch 2

- [ ] Use a ternary conditional expression at least once.
- [ ] Add replay or a second round.
- [ ] Use a helper function or nested conditional to keep the code readable.

## Submission Checklist

- [ ] Branch name is exactly `week-03-decision-quiz`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
