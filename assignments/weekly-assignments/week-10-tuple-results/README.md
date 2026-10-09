# Week 10 Future Assignment: Tuple Results And Records

## What You Are Building

Use tuples to return multiple related values from functions and store simple records.

## Textbook And Reference Sections

- Official textbook: Chapter 9, Tuples
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/tuples.html>
- Additional reference: <https://www.w3schools.com/python/python_tuples.asp>

## Concepts You Need

- A tuple groups values that belong together.
- Functions can return tuples when more than one result is useful.
- Tuple unpacking assigns tuple parts to separate names.
- Tuples are useful for records that should not be changed accidentally.

## Small Example

```python
def min_max(numbers):
    return min(numbers), max(numbers)
low, high = min_max([3, 8, 2])
```

## Requirements I Will Check

- [ ] Create at least one function that returns a tuple.
- [ ] Use tuple unpacking with the returned value.
- [ ] Create a list of at least three tuple records.
- [ ] Loop through the tuple records and print formatted output.
- [ ] Use at least one condition while processing the records.
- [ ] Calculate and print a summary value such as average, highest, or count.
- [ ] Use readable names for tuple parts after unpacking.
- [ ] `notes.md` explains when a tuple is a better fit than a list in this program.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Tuple return | 3 | Function returns and unpacks multiple values |
| Tuple records | 3 | Records are created and looped through |
| Summary logic | 2 | Computes a useful summary |
| Explanation | 2 | Notes explain tuple choice clearly |

## Stretch 1

- [ ] Add one more tuple-returning helper function.
- [ ] Sort records by one value before displaying them.
- [ ] Add one edge-case test.

## Stretch 2

- [ ] Combine lists and tuples in a small scoreboard.
- [ ] Let the user add a new tuple record from input.
- [ ] Find and display the best record according to your chosen rule.

## Submission Checklist

- [ ] Branch name is exactly `week-10-tuple-results`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
