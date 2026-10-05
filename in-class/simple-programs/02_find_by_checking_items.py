"""Practice 2: find a number by checking items.

Do not use `in`, `.index()`, `min()`, or `max()` for the search function.
The goal is to write the loop yourself.
"""

numbers = [42, 7, 19, 3, 88, 12, 7, 54, 31, 100, 23, 5, 67, 19, 2]


def find_number(values, target):
    """Return the index where target is found, or -1 if it is not found."""
    # TODO: loop through indexes from 0 to len(values) - 1
    # TODO: if values[index] equals target, return index
    # TODO: after the loop, return -1
    pass


def count_checks(values, target):
    """Return how many items are checked before the search stops."""
    checks = 0

    # TODO: loop through the values
    # TODO: add 1 to checks for each item checked
    # TODO: stop early if the item equals target

    return checks


print("Find 88:", find_number(numbers, 88))      # expected index: 4
print("Find 50:", find_number(numbers, 50))      # expected index: -1
print("Checks for 88:", count_checks(numbers, 88))
print("Checks for 50:", count_checks(numbers, 50))
