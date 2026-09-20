# Week 07 Future Assignment: Function Suite With Tests

## What You Are Building

Build a small suite of reusable functions and a demo/menu that lets a user try them.

## Textbook And Reference Sections

- Official textbook: Chapter 6, Fruitful functions
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html>
- Additional reference: <https://www.w3schools.com/python/python_functions.asp>

## Concepts You Need

- Fruitful functions use `return` to send an answer back.
- A function should do one clear job.
- Simple tests prove a function before it is used in a larger program.
- A menu combines input, conditionals, and function calls.

## Small Example

```python
def add_tax(subtotal, rate):
    return subtotal + subtotal * rate
```

## Requirements I Will Check

- [ ] Write at least four functions.
- [ ] At least three functions must return values.
- [ ] At least two functions must have parameters.
- [ ] Use a menu or clear demo section that calls every function.
- [ ] Include at least four test calls with expected results in comments or printed labels.
- [ ] Use meaningful function and variable names.
- [ ] Avoid repeated calculation code by calling functions instead.
- [ ] `notes.md` explains which function was hardest to test and why.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Function correctness | 4 | Functions return correct results for normal inputs |
| Testing | 2 | Expected outputs are shown or explained |
| Integration | 2 | Menu/demo calls every function |
| Code quality | 2 | Names and structure make the program readable |

## Stretch 1

- [ ] Add one function that validates input and returns `True` or `False`.
- [ ] Use that validation function before doing a calculation.
- [ ] Add two more tests for edge cases.

## Stretch 2

- [ ] Create a small command loop that keeps running until the user quits.
- [ ] Separate display, input, and calculation into different functions.
- [ ] Include one function that calls at least two other functions.

## Submission Checklist

- [ ] Branch name is exactly `week-07-function-suite`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
