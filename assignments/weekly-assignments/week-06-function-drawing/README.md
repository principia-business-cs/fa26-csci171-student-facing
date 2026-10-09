# Week 06 Future Assignment: Function Drawing Studio

## What You Are Building

Create a turtle drawing program that uses your own functions to break a drawing into reusable parts.

## Textbook And Reference Sections

- Official textbook: Chapter 4, Functions; Chapter 6, Fruitful functions
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/functions.html>
- Additional reference: <https://www.w3schools.com/python/python_functions.asp>

## Concepts You Need

- A function packages a named set of steps so you can reuse it.
- Parameters let one function draw different sizes, colors, or locations.
- A fruitful function returns a value another part of the program can use.
- A `main()` function keeps the program organized.

## Small Example

```python
def draw_square(artist, size):
    for side in range(4):
        artist.forward(size)
        artist.right(90)
```

## Requirements I Will Check

- [ ] Define and call at least three functions you wrote.
- [ ] Use at least one function with a parameter.
- [ ] Use at least one fruitful function that returns a value.
- [ ] Use a `for` loop inside at least one function.
- [ ] Use turtle movement and at least two turtle style commands.
- [ ] Use a `main()` function and call it at the bottom of the file.
- [ ] Add comments that explain each function's responsibility.
- [ ] `notes.md` includes one short test or explanation for the fruitful function.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Function design | 4 | Three focused functions, including a parameterized one |
| Return value | 2 | Fruitful function returns and is used correctly |
| Turtle output | 2 | Drawing is intentional and uses style commands |
| Organization/testing | 2 | Uses `main()` and explains or tests the return value |

## Stretch 1

- [ ] Add a second parameterized drawing function.
- [ ] Let the user choose a size or color.
- [ ] Use the returned value in a printed summary.

## Stretch 2

- [ ] Create a repeated scene using one function that calls another function.
- [ ] Use at least two parameters in one function.
- [ ] Keep the program readable with short, single-purpose functions.

## Submission Checklist

- [ ] Branch name is exactly `week-06-function-drawing`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
