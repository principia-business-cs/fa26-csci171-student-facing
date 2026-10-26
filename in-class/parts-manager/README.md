# Parts Desk: In-Class Inventory Manager

Your campus repair shop keeps losing track of screws, wheels, and motors. Build a terminal program that tells the team what is available and updates quantities when parts arrive or are used.

Work in pairs; switch the keyboard after each checkpoint. Each person should be able to explain how one object's quantity changes. This is in-class practice, not a required graded submission.

## Plan For Today

Allow about 80 minutes for the core: 15 for the class, 20 for the list/search, 30 for the menu, and 15 for testing. Use remaining time for extensions and discussion. Finish the core before adding extras.

Create `in-class/parts-manager/parts_manager.py` in your own repository. Download [starter.py](starter.py) into that file; do not connect your repository to the course repository. Optional practice branch: `in-class-parts-manager`.

## 1. Create The Part Class

Write `class Part` with these instance attributes:

| Attribute | Meaning | Example |
|---|---|---|
| `part_id` | Unique string identifier | `P101` |
| `name` | Part name | `Screw` |
| `quantity` | Whole units available | `20` |
| `price` | Price per unit | `0.25` |

Implement these methods:

- `__init__(self, part_id, name, quantity, price)` stores all four attributes.
- `restock(self, amount)` adds a positive whole-number amount and returns `True`. For zero or a negative amount, leave quantity unchanged and return `False`.
- `use(self, amount)` subtracts a positive whole-number amount only when enough stock exists. Return `True` on success; otherwise return `False` without changing quantity. Using exactly the available quantity is allowed.

Assume methods receive integers; validating terminal input comes later. Call methods on an object, for example `parts[0].restock(5)`. Do not put `input()` in the class.

**Checkpoint:** Create two objects. Restock one and show that the other object's quantity did not change. Explain what `self` refers to.

## 2. Build And Search The Inventory

Create a list named `parts` containing these objects:

| ID | Name | Quantity | Price |
|---|---|---:|---:|
| P101 | Screw | 20 | 0.25 |
| P102 | Wheel | 6 | 3.50 |
| P103 | Motor | 2 | 12.00 |

- Write `find_part(parts, part_id)` using a loop. Return the matching **Part object**, or `None` when not found. Strip spaces and ignore case in the entered ID.
- Write `show_parts(parts)` using a loop. Print each ID, name, quantity, and unit price. Format money to two decimal places.
- Mark quantities **below 5** as `LOW STOCK`; quantity 5 is not low.

**Checkpoint:** Searching for ` p102 ` returns the Wheel object. Searching for `P999` returns `None`. Why does changing the returned object also change the object in the list?

## 3. Build The Menu

In `main()`, use a `while` loop and `if`/`elif`/`else` to offer:

```text
1. Show parts
2. Find a part
3. Restock a part
4. Use a part
0. Quit
```

For options 2-4, ask for an ID and use `find_part`. If missing, print `Part not found` and return to the menu. For options 3-4, ask for an amount, call the object's method, and print whether the operation succeeded plus the current quantity.

- Reject blank input, letters, zero, and negative amounts without crashing or changing stock.
- The supplied `read_positive_int()` handles integer conversion; read it, but you do not have to write exception handling today.
- An unknown menu choice prints a message and repeats the menu.
- Create the inventory once, before the menu loop, so changes persist until quitting. No file storage is required.
- Quit with `0`; do not call the menu recursively.

## Core Checklist

- [ ] Three separate Part objects are stored in one list.
- [ ] Class methods change only the selected object's quantity.
- [ ] Search returns an object or `None`, using a list loop.
- [ ] All five menu choices work, with readable `print()` output.
- [ ] Restock/use reject invalid quantities; stock never becomes negative.
- [ ] Low-stock checks use `< 5`, not `<= 5`.
- [ ] State survives multiple menu actions; `main()` is called once.
- [ ] Run the tests below and record actual results in [notes.md](notes.md).

## Tests

Start fresh for each numbered test unless the actions describe a sequence.

| Test | Actions | Expected |
|---|---|---|
| 1 | Show initial inventory | Three rows; only Motor is LOW STOCK; prices 0.25, 3.50, 12.00 |
| 2 | Find ` p102 `; find P999 | Wheel details; then Part not found |
| 3 | Restock Motor by 4; use Motor by 1 | Quantities 6 then 5; no low-stock warning at 5 |
| 4 | Use all 6 Wheels; try using 1 more | Quantity 0; second request rejected; stays 0 |
| 5 | Restock/use with `0`, `-2`, blank, or `hello` | Rejected without crashing or changing stock |
| 6 | Enter menu choice 9, then show parts, then 0 | Invalid-choice message; inventory still available; program exits |

## Extension 1: Inventory Value (Moderate)

- Add `inventory_value(self)` returning `quantity * price`.
- Show each part's total value and a class-independent overall total computed by looping through `parts`.
- Initial total must be **50.00**. After using one Motor, total must be **38.00**.

## Extension 2: Add A New Part (Challenge)

- Add menu option 5 to collect a new ID, name, starting quantity, and price.
- Require nonempty ID/name, nonnegative whole-number quantity, and nonnegative finite numeric price. Reject bad input without changing the inventory.
- Reject duplicate IDs, ignoring case; append a new Part object only after all checks pass.
- Test adding P104/Bolt/10/0.50, rejecting `p104` again, and rejecting a price of `-1` or `hello`. If Extension 1 is complete, adding this part to the initial inventory gives **55.00**.

## Exit Reflection

In two or three sentences: What is the difference between the Part class, one Part object, and the parts list? Which method protects the inventory from invalid changes?

## Instructor Check-In (Not A Separate Grade)

| Area | Evidence |
|---|---|
| Objects and methods | Independent attributes; restock/use operate on `self` |
| Lists and search | Loops through objects; handles a missing match |
| Input and conditionals | Validates choices and quantities; rejects insufficient stock |
| Integration and testing | Menu preserves state; all six core tests demonstrated |
