# Week 11 Future Assignment: Utility Module

## What You Are Building

Create your own module of helper functions and import it into a second program.

## Textbook And Reference Sections

- Official textbook: Chapter 12, Modules
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/modules.html>
- Additional reference: <https://www.w3schools.com/python/python_modules.asp>

## Concepts You Need

- A module is a Python file that can be imported by another file.
- Modules help organize reusable code.
- The `import` statement gives one file access to functions from another file.
- A good module can be tested separately from the program that uses it.

## Small Example

```python
# utils.py
def shout(text):
    return text.upper() + '!'

# main.py
import utils
print(utils.shout('hello'))
```

## Requirements I Will Check

- [ ] Create a helper module file such as `utils.py`.
- [ ] Define at least three functions in the module.
- [ ] Create a second Python file that imports the module.
- [ ] Call every module function from the second file.
- [ ] At least two module functions must return values.
- [ ] Use `if __name__ == '__main__':` in at least one file.
- [ ] Print a clear demo of the module working.
- [ ] `notes.md` explains why the helper functions belong in a separate module.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Module structure | 3 | Two files are used with import correctly |
| Reusable functions | 3 | Module functions are focused and return values |
| Demo program | 2 | Second file calls every function clearly |
| Explanation | 2 | Notes explain modular design |

## Stretch 1

- [ ] Add simple tests for each helper function.
- [ ] Use aliases or selective imports carefully.
- [ ] Document each function with a short docstring.

## Stretch 2

- [ ] Create a small package-like folder or split helpers into two modules.
- [ ] Add input validation in the module, not just in the main file.
- [ ] Use the module in a second small demo program.

## Project Assigned This Week

- [Project 3: Final Integrated Python Program](./project-03-final-program/README.md)

## Submission Checklist

- [ ] Branch name is exactly `week-11-utility-module`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
