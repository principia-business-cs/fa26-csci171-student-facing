# Week 12 Future Assignment: File Tracker

## What You Are Building

Read a text file and generate a useful summary from its contents.

## Textbook And Reference Sections

- Official textbook: Chapter 13, Files
- Textbook section: <https://openbookproject.net/thinkcs/python/english3e/files.html>
- Additional reference: <https://www.w3schools.com/python/python_file_handling.asp>

## Concepts You Need

- Programs can read existing files with `open()`.
- A `with` block closes a file automatically.
- Looping through a file processes one line at a time.
- String cleanup is often needed before counting file contents.

## Small Example

```python
with open('sample_input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
```

## Requirements I Will Check

- [ ] Include a small sample text file in the assignment folder.
- [ ] Open and read the file using a `with` block.
- [ ] Loop through the file line by line.
- [ ] Count at least two things such as lines, words, non-empty lines, or keyword matches.
- [ ] Use `.strip()` or `.split()` while processing text.
- [ ] Print a labeled summary of the results.
- [ ] Handle the file name as a variable, not repeated string literals everywhere.
- [ ] `notes.md` includes the expected result for the sample file.

## Rubric

| Area | Points | Evidence |
|---|---:|---|
| File reading | 3 | Uses `with open(...)` and reads the intended file |
| Line processing | 3 | Loop and string methods compute correct counts |
| Summary output | 2 | Results are labeled and understandable |
| Testing | 2 | Expected sample result is documented |

## Stretch 1

- [ ] Ask the user which keyword to count.
- [ ] Ignore case when counting the keyword.
- [ ] Print the line numbers where the keyword appears.

## Stretch 2

- [ ] Write the summary to a new output file.
- [ ] Handle a missing file with a clear message.
- [ ] Use functions to separate reading, counting, and reporting.

## Submission Checklist

- [ ] Branch name is exactly `week-12-file-tracker`.
- [ ] Program runs before submitting.
- [ ] Pull request is open into your repo's `main` branch.
- [ ] PR link is submitted in Canvas.
