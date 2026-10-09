# Week 04 Future Assignment: Guessing Game With A Loop

## What You Are Building

Create a guessing game that keeps running until the user reaches a correct answer or a clear stopping condition.

## Textbook And Reference Sections

- Official textbook: Chapter 7, Iteration
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/iteration.html>
- Additional reference: <https://www.w3schools.com/python/python_while_loops.asp>

## Concepts You Need

- A `while` loop repeats while its condition is true.
- A sentinel or loop-control variable helps decide when to stop.
- Conditionals inside loops give feedback each round.
- Counters track how many times something happened.
- Good loops have a clear way to end.

## Small Example

```python
secret = 5
guess = 0
while guess != secret:
    guess = int(input('Guess: '))
```

## Requirements I Will Check

- [ ] Use a `while` loop.
- [ ] Use a sentinel or loop-control variable.
- [ ] Ask the user for guesses with `input()`.
- [ ] Convert guesses to numbers with `int()`.
- [ ] Give different feedback for too low, too high, and correct.
- [ ] Count the number of guesses.
- [ ] Print a final success message that includes the guess count.
- [ ] Avoid an accidental infinite loop.
- [ ] `notes.md` includes at least three test cases or a short trace of the loop.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Loop control | 4 | Loop starts, repeats, and stops correctly |
| Conditional feedback | 2 | Low/high/correct branches work |
| Counter | 2 | Attempts are counted accurately |
| Testing | 2 | Notes trace important loop paths |

## Stretch 1

- [ ] Add difficulty levels or a custom number range.
- [ ] Validate that the guess is inside the chosen range.
- [ ] Add two tests for the difficulty/range behavior.

## Stretch 2

- [ ] Add replay so the user can play more than once.
- [ ] Track the best score across rounds.
- [ ] Use a helper function for one part of the game if you know functions already.

## Submission Checklist

- [ ] Branch name is exactly `week-04-guessing-game`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
