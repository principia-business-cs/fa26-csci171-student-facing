# Week 13 Future Assignment: Event-Driven Turtle Toy

## What You Are Building

Create a small turtle program that responds to keyboard or mouse events.

## Textbook And Reference Sections

- Official textbook: Chapter 10, Event handling
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/events.html>
- Additional reference: <https://docs.python.org/3/library/turtle.html>

## Concepts You Need

- Event-driven programs wait for user actions.
- A callback function runs when an event happens.
- Turtle screens can listen for key presses and mouse clicks.
- Events combine functions, state changes, and user interaction.

## Small Example

```python
def turn_left():
    artist.left(30)

screen.onkey(turn_left, 'Left')
screen.listen()
```

## Requirements I Will Check

- [ ] Use at least three event bindings such as `onkey()` or `onclick()`.
- [ ] Write a separate callback function for each event.
- [ ] At least one event changes direction or position.
- [ ] At least one event changes color, size, or another visible state.
- [ ] Use `screen.listen()` when using keyboard events.
- [ ] Add short comments describing each event.
- [ ] Program remains open long enough to interact with it.
- [ ] `notes.md` lists the controls and what each one does.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Event bindings | 4 | At least three controls work |
| Callback design | 2 | Each event uses a named function |
| Interaction clarity | 2 | Controls visibly change the program |
| Documentation | 2 | Notes list controls and behavior |

## Stretch 1

- [ ] Add a reset key.
- [ ] Keep score or count how many actions happened.
- [ ] Display the count using turtle writing or console output.

## Stretch 2

- [ ] Create a simple drawing game or reaction challenge.
- [ ] Use both keyboard and mouse events.
- [ ] Organize repeated behavior with helper functions.

## Submission Checklist

- [ ] Branch name is exactly `week-13-event-toy`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
