# Week 14 Future Assignment: Final Project Checkpoint And List Algorithm

## What You Are Building

Create a project checkpoint program that stores several records and uses list algorithms to summarize or search them.

## Textbook And Reference Sections

- Official textbook: Chapter 14, List Algorithms
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>
- Additional reference: <https://www.w3schools.com/python/python_lists.asp>

## Concepts You Need

- List algorithms are repeatable patterns for searching, counting, summing, filtering, and finding best values.
- A checkpoint should prove that a larger project has working data and logic.
- Loops and conditionals are the heart of many data-processing programs.
- Clear test data makes a project easier to grade and improve.

## Small Example

```python
best = scores[0]
for score in scores:
    if score > best:
        best = score
```

## Requirements I Will Check

- [ ] Create a list with at least five records or values.
- [ ] Use a loop to process every item.
- [ ] Implement at least two list algorithms such as count, sum, search, filter, or best-so-far.
- [ ] Use at least one function for an algorithm.
- [ ] Print a checkpoint report with project title, data summary, and next step.
- [ ] Include at least three realistic test records.
- [ ] Use comments to identify which list algorithms you implemented.
- [ ] `notes.md` describes how this checkpoint could grow into a final project.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| List algorithms | 4 | Two algorithms work and are identifiable |
| Data design | 2 | Records are realistic and useful |
| Project connection | 2 | Checkpoint report explains next step |
| Testing/clarity | 2 | Test data and comments support grading |

## Stretch 1

- [ ] Let the user add one record before the report runs.
- [ ] Filter records by a user-chosen threshold or keyword.
- [ ] Print the filtered results separately.

## Stretch 2

- [ ] Save the checkpoint report to a text file.
- [ ] Use a nested list or tuple record structure.
- [ ] Separate input, algorithm, and reporting into functions.

## Submission Checklist

- [ ] Branch name is exactly `week-14-project-checkpoint`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
