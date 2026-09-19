# Week 04 Future Assignment: Guessing Game

## What You Are Building

Build a number guessing game that uses a loop to keep asking until the game ends.

## Textbook And Reference Sections

- Official textbook: Chapter 7, Iteration
- Textbook link: <https://openbookproject.net/thinkcs/python/english3e/iteration.html>
- W3Schools references:
  - Python While Loops: <https://www.w3schools.com/python/python_while_loops.asp>
  - Python Break: <https://www.w3schools.com/python/python_while_loops.asp>

## Concepts You Need

- A `while` loop repeats while a condition is true.
- `while True:` creates an intentional loop that must stop with `break`.
- `break` exits the nearest loop.
- A sentinel value is a special value that tells the program to stop.
- A counter variable can track attempts.

## Small Example

```python
while True:
    answer = input("Type quit to stop: ")
    if answer == "quit":
        break
    print("You typed", answer)
```

## Requirements I Will Check

- [ ] Use a `while` loop to repeat guesses.
- [ ] Use either a sentinel condition or `while True` with `break`.
- [ ] Ask for numeric input and convert it with `int()`.
- [ ] Use conditionals to print too high, too low, or correct.
- [ ] Track the number of guesses with a counter.
- [ ] Stop after the correct answer or quit condition.
- [ ] Print a final summary that includes the number of guesses.
- [ ] `notes.md` includes at least three test cases, including a win path and repeated wrong guesses.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Loop control | 4 | Loop repeats and stops correctly |
| Conditional feedback | 2 | Too high/too low/correct works |
| Counter and summary | 2 | Attempt count is accurate |
| Testing | 2 | Tests include different paths |

## Stretch 1

- [ ] Add difficulty levels with different ranges.
- [ ] Print the selected range before guessing starts.
- [ ] Add two more tests for difficulty levels.

## Stretch 2

- [ ] Add replay.
- [ ] Track best score during one run.
- [ ] Use a helper function or nested loop to keep the code readable.

## Submission Checklist

- [ ] Branch name is exactly `week-04-guessing-game`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
