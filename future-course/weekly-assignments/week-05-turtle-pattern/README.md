# Week 05 Future Assignment: Turtle Pattern Drawing

## What You Are Building

Draw a repeated turtle pattern using loops. This future version also prepares students for Mini Project 1: Turtle Sketch And Pattern.

## Textbook And Reference Sections

- Official textbook: Chapter 3, Hello, little turtles
- Official textbook: Chapter 7, Iteration
- Turtle chapter link: <https://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html>
- Iteration chapter link: <https://openbookproject.net/thinkcs/python/english3e/iteration.html>
- Python turtle reference: <https://docs.python.org/3/library/turtle.html>
- W3Schools for loops reference: <https://www.w3schools.com/python/python_for_loops.asp>

## Concepts You Need

- `for` loops repeat a known number of times.
- `range()` creates a sequence of numbers for a loop.
- Turtle movement commands include `forward()`, `left()`, and `right()`.
- Turtle drawing can use color, fill, pen size, and position.
- Repetition should come from loops, not copied lines.

## Small Example

```python
import turtle

artist = turtle.Turtle()
for side in range(4):
    artist.forward(100)
    artist.right(90)

turtle.done()
```

## Requirements I Will Check

- [ ] Import `turtle` and create a turtle object.
- [ ] Use at least one `for` loop with `range()`.
- [ ] Draw a repeated shape or pattern with at least six repeated movements.
- [ ] Use turtle movement commands such as `forward()`, `left()`, or `right()`.
- [ ] Use at least one variable to control size, side count, or repeat count.
- [ ] Change direction inside the loop so the drawing forms a visible pattern.
- [ ] End with `turtle.done()` or an equivalent screen exit call.
- [ ] `notes.md` includes at least three test notes about changing size, angle, or repetitions.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Turtle basics | 2 | Turtle object and drawing commands work |
| Loop use | 3 | Repetition comes from `for` loops |
| Pattern quality | 2 | Output is intentional and visible |
| Variables and testing | 3 | Variables control drawing and notes show tests |

## Stretch 1

- [ ] Add at least two colors or pen sizes.
- [ ] Use a second loop to draw more than one copy of the base shape.
- [ ] Keep the drawing readable, not just a scribble.

## Stretch 2

- [ ] Use nested loops to create a geometric design.
- [ ] Use variables for both inner and outer loop counts.
- [ ] Add a short comment explaining the nested-loop structure.

## Submission Checklist

- [ ] Branch name is exactly `week-05-turtle-pattern`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
