# Week 15 Future Assignment: Small Class Model

## What You Are Building

Create a small class that models something in your project or daily life, then create objects from it.

## Textbook And Reference Sections

- Official textbook: Chapter 15, Classes and Objects - the Basics
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>
- Additional reference: <https://www.w3schools.com/python/python_classes.asp>

## Concepts You Need

- A class defines a new type of thing for your program.
- An object is one instance of a class.
- Attributes store object data.
- Methods are functions that belong to objects.

## Small Example

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
```

## Requirements I Will Check

- [ ] Define one class with a clear name.
- [ ] Use `__init__` to set at least three attributes.
- [ ] Write at least two methods besides `__init__`.
- [ ] Create at least three objects from the class.
- [ ] Call methods on the objects and print the results.
- [ ] Use a list to store the objects.
- [ ] Loop through the object list to display summaries.
- [ ] `notes.md` explains what real-world idea your class represents.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| Class design | 3 | Class, attributes, and constructor are correct |
| Methods | 3 | Methods use object state meaningfully |
| Object use | 2 | Multiple objects are created and looped through |
| Explanation | 2 | Notes explain the model clearly |

## Stretch 1

- [ ] Add a method that changes an attribute.
- [ ] Add a method that returns a calculated value.
- [ ] Use that returned value in a report.

## Stretch 2

- [ ] Create two related classes or one class that contains a list of items.
- [ ] Add a search or filter over the object list.
- [ ] Use your class as part of your final project idea.

## Submission Checklist

- [ ] Branch name is exactly `week-15-small-class`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
