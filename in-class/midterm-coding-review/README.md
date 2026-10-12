# Midterm Coding Review

Use this review to practice for the coding portion of the midterm. These are not the exam questions. They are practice problems for the same core skills:

- writing functions with exact names
- using conditionals with ranges
- looping through lists and tuples
- counting matching values
- building dictionaries from data
- looping through `.items()`
- using `main()` to test your code

## How We Will Use This In Class

Open `starter.py`. We will write the code together during class.

Write each function above `main()`. Keep the function names exactly as written so we can test the code together.

## Required Function Names

- `attendance_message(days_present, total_days)`
- `count_scores_at_least(scores, target)`
- `build_inventory_value(items)`
- `average(values)`
- `print_club_summary(club_hours)`
- `main()`

## Problem 1: Attendance Message

Write a function named `attendance_message(days_present, total_days)`.

The function should calculate the attendance percentage:

```python
days_present / total_days
```

Return one of these exact strings:

- `"excellent attendance"` when attendance is at least 90%
- `"steady attendance"` when attendance is at least 75% but less than 90%
- `"needs a plan"` when attendance is below 75%

This practices division, comparison operators, and conditionals with ranges.

## Problem 2: Count Scores At Least A Target

Write a function named `count_scores_at_least(scores, target)`.

The function should return how many scores in the list are greater than or equal to `target`.

Example:

```python
count_scores_at_least([82, 91, 77, 100, 88], 85)
```

should return:

```python
3
```

Rules:

- Start a counter at `0`.
- Use a loop.
- Use an `if` statement inside the loop.
- Return the final counter.

This practices a common pattern: count the things that match a condition.

## Problem 3: Build Inventory Values

Write a function named `build_inventory_value(items)`.

The `items` list contains tuples. Each tuple has:

```python
(item_name, price, quantity)
```

The function should return a dictionary where each item name maps to the total value for that item:

```python
price * quantity
```

Example:

```python
build_inventory_value([
    ("notebook", 2.50, 4),
    ("pen", 1.25, 10),
])
```

should return:

```python
{"notebook": 10.0, "pen": 12.5}
```

Rules:

- Start with an empty dictionary.
- Use a loop.
- Unpack each tuple into clear variable names.
- Do not hardcode the final dictionary.

This practices tuples, dictionaries, and calculations inside loops.

## Problem 4: Club Hours Summary

Write a function named `average(values)` that returns the average of a list of numbers.

Then write a function named `print_club_summary(club_hours)`.

`club_hours` is a dictionary where:

- each key is a club name
- each value is a list of weekly practice hours

For each club, print the club name, average hours, and one label:

- `"on track"` when the average is at least 3
- `"check in"` when the average is below 3

Example style:

```text
Robotics average: 3.33 - on track
Chess average: 2.33 - check in
```

This practices helper functions, dictionary `.items()`, averages, and conditionals inside a report.

## Required Main Function

Use this exact `main()` function at the bottom of your file:

```python
def main():
    print("Problem 1")
    print(attendance_message(18, 20))
    print(attendance_message(15, 20))
    print(attendance_message(10, 20))

    print("\nProblem 2")
    print(count_scores_at_least([82, 91, 77, 100, 88], 85))
    print(count_scores_at_least([70, 72, 74], 75))

    print("\nProblem 3")
    inventory = [
        ("notebook", 2.50, 4),
        ("pen", 1.25, 10),
        ("folder", 3.00, 2),
    ]
    print(build_inventory_value(inventory))

    print("\nProblem 4")
    club_hours = {
        "Robotics": [3, 4, 3],
        "Chess": [2, 2, 3],
        "Choir": [4, 4, 5],
    }
    print_club_summary(club_hours)


if __name__ == "__main__":
    main()
```

## Quick Self-Check

- [ ] Each required function exists with the exact name.
- [ ] Each function returns or prints what the prompt asks for.
- [ ] The code runs without syntax errors.
- [ ] `main()` calls all review functions.
- [ ] The report output is easy for a human to read.
