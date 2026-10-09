# Week 02 Future Assignment: Friendly Calculator

## What You Are Building

Create a useful calculator that collects input, converts values, performs arithmetic, and prints a labeled summary.

## Textbook And Reference Sections

- Official textbook: Chapter 2, Variables, expressions and statements
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>
- Additional reference: <https://www.w3schools.com/python/python_operators.asp>

## Concepts You Need

- `input()` always starts as text.
- `int()` and `float()` convert text into numbers.
- Arithmetic expressions can combine variables and operators.
- A good calculator stores intermediate values with clear names.
- Readable output matters as much as getting the number right.

## Small Example

```python
price = float(input('Price: '))
quantity = int(input('Quantity: '))
print('Subtotal:', price * quantity)
```

## Requirements I Will Check

- [ ] Ask for at least three inputs.
- [ ] Use `float()` at least once.
- [ ] Use `int()` at least once.
- [ ] Use at least three arithmetic operators from `+`, `-`, `*`, `/`, `//`, `%`, or `**`.
- [ ] Store at least two intermediate results in variables.
- [ ] Print a labeled final summary with at least three lines.
- [ ] Round or format money-like values when appropriate.
- [ ] `notes.md` includes two test cases with inputs and expected results.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Input/conversion | 3 | Uses input plus numeric conversion correctly |
| Arithmetic | 3 | Computes required results accurately |
| Readable output | 2 | Summary labels are clear |
| Testing | 2 | Two test cases are documented |

## Stretch 1

- [ ] Add a tip, discount, or unit conversion option.
- [ ] Add one more calculated summary value.
- [ ] Document one edge case in `notes.md`.

## Stretch 2

- [ ] Add a small menu with at least two calculator modes.
- [ ] Use conditionals if you know them already, or write two clearly separated calculator sections if not.
- [ ] Explain in `notes.md` how a user chooses what to calculate.

## Submission Checklist

- [ ] Branch name is exactly `week-02-calculator`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
