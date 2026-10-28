# Week 10: Campus Library Checkout

**Individual in-class assignment | 10 points | Submit by the end of class**

Build a terminal program for a small campus lending library. A librarian should be able to see the books, find a book, check it out, return it, and see a summary. Write your program from a blank file; no starter is provided.

## Time Plan

- First 20 minutes: Book class and initial objects.
- Next 20 minutes: search and display functions.
- Next 35 minutes: interactive menu and checkout/return behavior.
- Next 20 minutes: tests and notes.
- Final 15 minutes: finish, commit, push, and submit.

Complete the core before attempting either extension. You may discuss concepts, but write and test your own code.

## Required Class And Methods

Define `class Book` with `__init__(self, book_id, title, author)`. Each object stores `book_id`, `title`, `author`, and `is_available`, initially `True`.

Implement these methods. Decide how to organize their logic yourself:

- `check_out(self)`: attempt to borrow this book. Return a Boolean indicating success.
- `return_book(self)`: attempt to return this book. Return a Boolean indicating success.

Keep `input()` and `print()` outside these methods. The methods change the object and return whether the action succeeded.

## Starting Books

Your list named `books` must contain three separate Book objects:

| Book ID | Title | Author |
|---|---|---|
| B101 | The Hobbit | J. R. R. Tolkien |
| B102 | A Wrinkle in Time | Madeleine L'Engle |
| B103 | The Little Prince | Antoine de Saint-Exupery |

Book status must persist between menu actions during one run.

## Required Functions

| Function | Required behavior |
|---|---|
| `find_book(books, book_id)` | Return the matching Book object, or `None`. Accept IDs regardless of surrounding spaces or letter case. |
| `show_books(books)` | Display each ID, title, author, and status: `Available` or `Checked out`. |
| `library_summary(books)` | Return the tuple `(available_count, checked_out_count)`. Do not print inside this function. |
| `main()` | Coordinate user interaction and the other functions. |

Your program must demonstrate list iteration, tuple unpacking, and calls to the object's methods. Choose the implementation yourself.

## User Experience

Provide these menu choices:

```text
1. Show all books
2. Find a book
3. Check out a book
4. Return a book
5. Show library summary
0. Quit
```

Users identify a book by its ID. An unknown ID produces `Book not found`.

Checkout succeeds only for an available book; return succeeds only for a checked-out book. Print a clear success or failure message. Rejected actions must not change inventory, and successful actions affect only the selected book.

The menu repeats until the user quits. Invalid choices, letters, blank input, and unknown IDs produce a helpful message without crashing. Use input, output, loops, and conditionals to achieve this. File saving is not required.

## Requirements Checklist

- [ ] Book has four instance attributes and two correctly functioning methods.
- [ ] `books` is a list containing three separate objects.
- [ ] `find_book` uses a loop and returns an object or `None`.
- [ ] Search accepts ` b102 ` as well as `B102`.
- [ ] Display includes all four required book details.
- [ ] Menu implements choices 0-5 and repeats after actions.
- [ ] Checkout/return use the object's methods and preserve other books' state.
- [ ] Summary returns a tuple and the caller unpacks it.
- [ ] Invalid input and repeated actions are handled without crashing.
- [ ] The six core tests below have actual results recorded in `notes.md`.

## Test Your Program

Use a fresh run for each test except where a sequence is specified.

| Test | Actions | Expected result |
|---|---|---|
| 1 | Show books, then summary | All three available; counts `(3, 0)` |
| 2 | Find ` b102 `, then `B999` | A Wrinkle in Time; then Book not found |
| 3 | Check out B101, show books, then summary | Only B101 checked out; counts `(2, 1)` |
| 4 | Check out B101 twice | First succeeds, second fails; counts remain `(2, 1)` |
| 5 | Check out B101, return it twice | First return succeeds, second fails; counts remain `(3, 0)` |
| 6 | Enter `9`, `hello`, blank menu input, blank search ID, then `0` | Helpful messages, no crash or changed books; clean exit |

In `notes.md`, record each test's actual outcome and pass/fail. Then explain in two or three sentences how the Book class differs from a Book object and from the books list.

## Rubric: 10 Points

| Area | Points | What earns credit |
|---|---:|---|
| Class and methods | 3 | Instance attributes (1), checkout behavior (1), return behavior (1) |
| Collections and functions | 3 | Object list and search (1), full display (1), tuple summary and unpacking (1) |
| Menu and integration | 2 | All choices and persistent state (1), invalid input/repeated actions handled (1) |
| Testing and explanation | 2 | Six documented tests (1), class/object/list explanation and readable code (1) |

## Extension 1: Available Titles (Moderate)

- Write `available_titles(books)` returning a new list of titles for available books only. Do not change the original books list.
- Add menu option 6 to display the result.
- Test initially (three titles), after checking out B102 (two titles, excluding A Wrinkle in Time), and after checking out all books (empty list).

## Extension 2: Borrower Records (Challenge)

- Store checked-out books in a dictionary named `borrowers`, mapping book IDs to borrower names.
- Ask for a nonblank borrower name before completing a checkout. Only record the borrower when checkout succeeds. A failed repeated checkout must not overwrite the original borrower.
- A successful return removes the corresponding borrower entry. Display borrower names beside checked-out books.
- Test B101 checked out to Jordan, a rejected second checkout to Sam (Jordan remains), and a return (entry removed). Test a blank name leaves the book available and creates no entry.

Attempt extensions after the core. Submit them in the same program; they are not separate grade items. The core rubric above determines the 10-point grade.

## Submit Before Leaving Class

1. Create branch **`week-10-library-checkout`** from your updated `main`.
2. Put your program at **`in-class/week-10-library/library.py`** and your test record at **`in-class/week-10-library/notes.md`** in your own repository.
3. Commit and push that branch; open a PR into your repository's `main`.
4. Submit the PR URL in Canvas for this in-class assignment. Do not submit a course-repository link.

This is a separate in-class activity. The original Week 10 tuple assignment remains unchanged.
