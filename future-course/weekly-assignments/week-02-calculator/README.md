# Week 02 Future Assignment: Friendly Calculator

## What You Are Building

Build a friendly calculator that asks for numbers, converts input to numeric values, stores results in variables, and prints labeled results.

## Textbook And Reference Sections

- Official textbook: Chapter 2, Variables, expressions and statements
- Textbook link: <https://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>
- W3Schools references:
  - Python Variables: <https://www.w3schools.com/python/python_variables.asp>
  - Python Numbers: <https://www.w3schools.com/python/python_numbers.asp>
  - Python Casting: <https://www.w3schools.com/python/python_casting.asp>

## Concepts You Need

- `input()` returns text, even if the user types a number.
- `int()` and `float()` convert text to numbers.
- Variables store values so you can reuse them.
- Arithmetic operators include `+`, `-`, `*`, `/`, `//`, `%`, and `**`.

## Small Example

```python
price = float(input("Price: "))
tax = price * 0.08
print("Tax:", tax)
```

## Requirements I Will Check

- [ ] Ask the user for at least two numeric inputs.
- [ ] Convert input with `int()` or `float()` before doing math.
- [ ] Store inputs in clearly named variables.
- [ ] Calculate at least four results.
- [ ] Print each result with a clear label.
- [ ] Use at least three different arithmetic operators.
- [ ] Handle or avoid division by zero in a clear way.
- [ ] `notes.md` includes at least three test cases, including decimals or zero.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Numeric input and conversion | 3 | Uses `int()` or `float()` correctly |
| Calculations | 3 | At least four correct labeled results |
| Variables and readability | 2 | Clear variable names and output labels |
| Testing | 2 | `notes.md` covers normal and tricky cases |

## Stretch 1

- [ ] Add a tip/split calculator or unit conversion mode.
- [ ] Use at least one additional input.
- [ ] Add two more tests for the new mode.

## Stretch 2

- [ ] Add a simple menu so the user can choose the calculation type.
- [ ] Use `if`/`elif`/`else` if those have been introduced, or clearly mark this as preview work.
- [ ] Keep the original required calculator working.

## Submission Checklist

- [ ] Branch name is exactly `week-02-calculator`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
