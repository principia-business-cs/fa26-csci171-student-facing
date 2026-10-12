# Midterm Coding Review

Use this review to practice for the coding portion of the midterm. These are not the exam questions, but they use the same kinds of thinking:

- functions with exact names
- conditionals
- loops over lists and tuples
- building dictionaries
- using lists inside dictionaries
- printing a clear report from a `main()` function

## How We Will Use This In Class

Open `starter.py`. We will write the code together during class.

Write each function above `main()`. Keep the function names exactly as written so we can test the code together.

## Required Function Names

- `shipping_zone(distance_miles)`
- `first_long_name(names)`
- `build_letter_counts(words)`
- `average(scores)`
- `print_team_report(team_scores)`
- `main()`

## Problem 1: Shipping Zone

Write a function named `shipping_zone(distance_miles)` that returns one of these exact strings:

- `"local"` when the distance is less than 25
- `"regional"` when the distance is at least 25 and less than 100
- `"national"` when the distance is at least 100 and less than 500
- `"long distance"` when the distance is 500 or more

This practices conditionals with ranges.

## Problem 2: First Long Name

Write a function named `first_long_name(names)` that takes a tuple of names and returns the first name with more than 6 characters.

Rules:

- Use a loop.
- Do not use `max()`.
- If no name has more than 6 characters, return `"none found"`.

This practices loops, strings, `len()`, and returning early from a function.

## Problem 3: Build Letter Counts

Write a function named `build_letter_counts(words)` that takes a list of words and returns a dictionary.

The dictionary should map each word to the number of letters in that word.

Example:

```python
build_letter_counts(["sun", "moon", "stars"])
```

should return:

```python
{"sun": 3, "moon": 4, "stars": 5}
```

Rules:

- Start with an empty dictionary.
- Use a loop.
- Do not hardcode the final dictionary.

This practices dictionary building.

## Problem 4: Team Score Report

Write a function named `average(scores)` that returns the average of a list of scores.

Then write a function named `print_team_report(team_scores)` that loops through `team_scores.items()` and prints each team name and average score.

Example style:

```text
Blue average: 8.67
Gold average: 7.33
```

This practices dictionaries whose values are lists.

## Required Main Function

Use this exact `main()` function at the bottom of your file:

```python
def main():
    print("Problem 1")
    print(shipping_zone(10))
    print(shipping_zone(25))
    print(shipping_zone(120))
    print(shipping_zone(700))

    print("\nProblem 2")
    print(first_long_name(("Ana", "Bo", "Caroline", "Dee")))
    print(first_long_name(("Mia", "Noor", "Kai")))

    print("\nProblem 3")
    word_lengths = build_letter_counts(["sun", "moon", "stars"])
    print(word_lengths)

    print("\nProblem 4")
    team_scores = {
        "Blue": [9, 8, 9],
        "Gold": [7, 8, 7],
        "Green": [10, 9, 8],
    }
    print_team_report(team_scores)


if __name__ == "__main__":
    main()
```

## Quick Self-Check

- [ ] Each required function exists with the exact name.
- [ ] Each function returns or prints what the prompt asks for.
- [ ] The code runs without syntax errors.
- [ ] `main()` calls all review functions.
- [ ] The report output is easy for a human to read.
