"""Practice 3: find a number faster in a sorted list.

The list is already sorted. Use that fact.

Rules:
- Do not use `in`.
- Do not use `.index()`.
- Do not loop through every value from left to right.
- Each step should check the middle of the remaining search area.
"""

numbers = [
    1, 2, 3, 5, 7, 8, 10, 12, 14, 15,
    18, 19, 21, 23, 25, 27, 30, 31, 33, 35,
    38, 40, 42, 44, 47, 50, 52, 54, 57, 60,
    63, 65, 67, 70, 72, 75, 78, 80, 83, 85,
    88, 90, 92, 94, 96, 97, 98, 99, 100
]


def find_in_sorted_list(values, target):
    """Return the index of target, or -1 if target is not found."""
    left = 0
    right = len(values) - 1

    while left <= right:
        # TODO: calculate the middle index between left and right
        middle = None

        # TODO: get the value at the middle index
        middle_value = None

        # TODO: if middle_value is target, return middle

        # TODO: if target is smaller than middle_value,
        # move right so the next search keeps only the left half

        # TODO: otherwise, move left so the next search keeps only the right half

        # Remove this line after you write the loop logic.
        break

    return -1


def trace_search(values, target):
    """Print each middle value checked while searching."""
    left = 0
    right = len(values) - 1
    checks = 0

    while left <= right:
        # TODO: calculate middle
        middle = None
        middle_value = None
        checks += 1

        print("check", checks, "index", middle, "value", middle_value)

        # TODO: use the same decision logic as find_in_sorted_list

        # Remove this line after you write the loop logic.
        break

    print("total checks:", checks)


print("Find 42:", find_in_sorted_list(numbers, 42))    # expected index: 22
print("Find 100:", find_in_sorted_list(numbers, 100))  # expected index: 48
print("Find 4:", find_in_sorted_list(numbers, 4))      # expected index: -1

trace_search(numbers, 42)
