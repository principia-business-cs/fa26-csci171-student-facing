# Week 08 Future Assignment: Text Analyzer

## What You Are Building

Create a text analyzer that reports facts about a user-entered sentence or short paragraph.

## Textbook And Reference Sections

- Official textbook: Chapter 8, Strings
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/strings.html>
- Additional reference: <https://www.w3schools.com/python/python_strings.asp>

## Concepts You Need

- Strings are sequences, so indexing and slicing work on them.
- String methods such as `.lower()`, `.strip()`, and `.count()` help clean and inspect text.
- A loop can visit each character in a string.
- Programs can calculate text statistics without advanced tools.

## Small Example

```python
text = input('Text: ').strip()
print('Lowercase:', text.lower())
print('First three:', text[:3])
```

## Requirements I Will Check

- [ ] Ask the user for a sentence or short paragraph.
- [ ] Use `.strip()` and `.lower()` or another string method.
- [ ] Print the total number of characters.
- [ ] Print the first and last character safely when text is not empty.
- [ ] Use a loop to count vowels or another character category.
- [ ] Use slicing at least once.
- [ ] Print a readable summary of at least four text facts.
- [ ] `notes.md` includes two test strings and expected observations.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| String methods | 3 | Uses methods for cleanup or analysis |
| Indexing/slicing | 2 | Uses sequence access safely |
| Loop analysis | 3 | Counts characters or categories correctly |
| Testing | 2 | Two test strings are documented |

## Stretch 1

- [ ] Count words using `.split()`.
- [ ] Report the longest word length.
- [ ] Ignore case when counting a chosen letter.

## Stretch 2

- [ ] Create a simple readability or strength score.
- [ ] Use functions to separate counting from printing.
- [ ] Handle empty input with a helpful message.

## Project Assigned This Week

- [Project 2: Functions And Loops Visual Builder](./project-02-functions-loops/README.md)

## Submission Checklist

- [ ] Branch name is exactly `week-08-text-analysis`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
