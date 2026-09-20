# Week 05 Future Assignment: Turtle Pattern With Loops

## What You Are Building

Create a turtle drawing that uses loops to make a repeated pattern, image, or small scene.

## Textbook And Reference Sections

- Official textbook: Chapter 3, Hello, little turtles!; Chapter 7, Iteration
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html>
- Additional reference: <https://docs.python.org/3/library/turtle.html>

## Concepts You Need

- Turtle commands move a visible drawing cursor.
- A `for` loop is useful when you know how many repeats you want.
- `range()` provides repeat counts for loops.
- Style commands such as color and fill make output easier to understand.
- Repeated drawing is a visual way to see loops working.

## Small Example

```python
for side in range(4):
    artist.forward(80)
    artist.right(90)
```

## Requirements I Will Check

- [ ] Use the turtle library.
- [ ] Use at least one `for` loop with `range()`.
- [ ] Draw at least one repeated shape or repeated visual element.
- [ ] Use `forward()` and a turn command such as `left()` or `right()`.
- [ ] Use at least two turtle style commands such as `pencolor()`, `fillcolor()`, `pensize()`, or `speed()`.
- [ ] Use `penup()`, `pendown()`, or `goto()` to move without drawing at least once.
- [ ] Add comments explaining the loop and the pattern it creates.
- [ ] `notes.md` explains what part of the drawing is controlled by the loop.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Loop use | 3 | Uses `for` and `range()` correctly |
| Turtle commands | 3 | Movement and style commands are used correctly |
| Drawing clarity | 2 | Output is recognizable and intentional |
| Explanation | 2 | Comments/notes explain the repeated pattern |

## Stretch 1

- [ ] Use `begin_fill()` and `end_fill()`.
- [ ] Draw the repeated pattern in at least two colors.
- [ ] Let the user choose one color, size, or count.

## Stretch 2

- [ ] Define and call at least one drawing function if you know functions already.
- [ ] Make one function call another function.
- [ ] Use a turtle feature from the official documentation that was not shown in class.

## Submission Checklist

- [ ] Branch name is exactly `week-05-turtle-pattern`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
