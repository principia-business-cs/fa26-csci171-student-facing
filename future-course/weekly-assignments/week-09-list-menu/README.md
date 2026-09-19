# Week 09 Future Assignment: List Menu Manager

## What You Are Building

Build a menu-driven list manager for tasks, study topics, inventory items, or another useful collection.

## Textbook And Reference Sections

- Official textbook: Chapter 11, Lists
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/lists.html>
- Additional reference: <https://www.w3schools.com/python/python_lists.asp>

## Concepts You Need

- A list stores multiple values in one variable.
- List methods such as `.append()` and `.remove()` change the list.
- A loop can display every item in a list.
- A menu loop lets the user keep working until they choose to quit.

## Small Example

```python
items = []
items.append('read chapter')
for item in items:
    print('-', item)
```

## Requirements I Will Check

- [ ] Start with a list containing at least two items.
- [ ] Use a loop that keeps showing a menu until the user quits.
- [ ] Let the user add an item with `.append()`.
- [ ] Let the user remove an item safely.
- [ ] Display all items using a loop.
- [ ] Use an `if` / `elif` / `else` chain for menu choices.
- [ ] Print a helpful message for invalid choices.
- [ ] `notes.md` includes a short transcript or test plan.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| List operations | 4 | Add, remove, and display work correctly |
| Menu loop | 2 | Program repeats until quit |
| Error handling | 2 | Invalid choices and missing items are handled |
| Testing | 2 | Transcript/test plan shows major paths |

## Stretch 1

- [ ] Add an option to count items or mark one complete.
- [ ] Prevent blank items from being added.
- [ ] Sort or reverse the list before displaying it.

## Stretch 2

- [ ] Store each item as a nested list with a name and priority.
- [ ] Let the user update the priority.
- [ ] Display items in a formatted table.

## Submission Checklist

- [ ] Branch name is exactly `week-09-list-menu`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
