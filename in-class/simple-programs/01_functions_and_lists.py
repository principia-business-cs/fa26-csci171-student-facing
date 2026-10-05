"""Practice 1: functions and lists.

Run this file, then complete each TODO.
"""

scores = [88, 72, 95, 63, 100, 81, 77, 90]


def print_scores(values):
    """Print each score on its own line."""
    # TODO: loop through values and print each score
    pass


def count_scores(values):
    """Return how many scores are in the list."""
    # TODO: return the length of the list
    pass


def find_biggest(values):
    """Return the largest score in the list."""
    # TODO: start with the first value, then loop and update biggest when needed
    pass


def count_passing(values):
    """Return how many scores are 70 or higher."""
    # TODO: count the values that are >= 70
    pass


print("Scores:")
print_scores(scores)

print("Count:", count_scores(scores))
print("Biggest:", find_biggest(scores))
print("Passing:", count_passing(scores))
