"""
CSCI171 conditionals mini-programs

Use these as short live-coding examples. Each example is intentionally small.
Run one function at a time from main() by uncommenting the call you want.
"""


def example_01_plain_if():
    """A single if statement: code runs only when the condition is True."""
    temperature = 85

    print("Checking the weather...")
    if temperature >= 80:
        print("It is warm today.")

    print("Done checking.")


def example_02_if_else():
    """if/else: choose between two paths."""
    age = int(input("Age: "))

    if age >= 18:
        print("You can vote in many elections.")
    else:
        print("You are not 18 yet.")


def example_03_comparison_operators():
    """Practice ==, !=, <, <=, >, >=."""
    score = int(input("Quiz score: "))

    if score == 10:
        print("Perfect score")
    if score != 10:
        print("Not perfect yet")
    if score >= 7:
        print("Passing score")
    if score < 7:
        print("Keep practicing")


def example_04_if_elif_else():
    """elif: choose one path from several options."""
    grade = int(input("Grade percent: "))

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("Not passing yet")


def example_05_order_matters():
    """A teaching example: condition order changes the result."""
    grade = 95

    print("Wrong order:")
    if grade >= 60:
        print("D or better")
    elif grade >= 90:
        print("A")

    print("Better order:")
    if grade >= 90:
        print("A")
    elif grade >= 60:
        print("D or better")


def example_06_boolean_and():
    """and: both conditions must be True."""
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "student" and password == "python":
        print("Welcome")
    else:
        print("Login failed")


def example_07_boolean_or():
    """or: at least one condition must be True."""
    day = input("Day of week: ").strip().lower()

    if day == "saturday" or day == "sunday":
        print("Weekend")
    else:
        print("Weekday")


def example_08_boolean_not():
    """not: flips True to False, or False to True."""
    has_homework = input("Do you have homework? yes/no: ").strip().lower()

    if not has_homework == "yes":
        print("Enjoy the free time.")
    else:
        print("Make a plan and start small.")


def example_09_input_cleanup():
    """strip() and lower() make user input easier to compare."""
    answer = input("Do you want to continue? yes/no: ").strip().lower()

    if answer == "yes" or answer == "y":
        print("Continuing...")
    elif answer == "no" or answer == "n":
        print("Stopping...")
    else:
        print("I did not understand that answer.")


def example_10_nested_if():
    """Nested if: a decision inside another decision."""
    has_ticket = input("Do you have a ticket? yes/no: ").strip().lower()

    if has_ticket == "yes":
        age = int(input("Age: "))
        if age >= 18:
            print("You may enter the evening show.")
        else:
            print("You may enter the afternoon show.")
    else:
        print("Please buy a ticket first.")


def example_11_range_check():
    """Check whether a number is inside a valid range."""
    rating = int(input("Rate this class from 1 to 5: "))

    if 1 <= rating <= 5:
        print("Valid rating:", rating)
    else:
        print("Rating must be from 1 to 5.")


def example_12_membership_with_in():
    """in can test whether a value is one of several choices."""
    choice = input("Choose rock, paper, or scissors: ").strip().lower()

    if choice in ["rock", "paper", "scissors"]:
        print("You chose", choice)
    else:
        print("That is not a valid choice.")


def example_13_common_bug_assignment_vs_comparison():
    """Common bug: = assigns, == compares. This shows the correct version."""
    secret = "python"
    guess = input("Secret word: ").strip().lower()

    # Correct: use == to compare two values.
    if guess == secret:
        print("Correct")
    else:
        print("Try again")


def example_14_common_bug_indentation():
    """Indentation controls what belongs inside the if block."""
    score = 8

    if score >= 7:
        print("Passing")
        print("This line is inside the if block.")

    print("This line always runs because it is not indented inside the if.")


def example_15_truthy_values():
    """Empty strings are False-like; non-empty strings are True-like."""
    name = input("Name: ").strip()

    if name:
        print("Hello,", name)
    else:
        print("You did not type a name.")


def example_16_mini_project_decision_helper():
    """Tiny project: recommend what to do based on time and energy."""
    minutes = int(input("How many free minutes do you have? "))
    energy = input("Energy level: low, medium, high: ").strip().lower()

    if minutes < 10:
        print("Do one tiny task: open your file and read the instructions.")
    elif minutes < 30 and energy == "low":
        print("Review notes or fix one small bug.")
    elif minutes < 30:
        print("Complete one function or one small feature.")
    elif energy == "high":
        print("Work on the challenge extension.")
    else:
        print("Finish the required assignment first.")


def example_17_challenge_simple_quiz():
    """Challenge: combine score, input cleanup, and if/elif/else."""
    score = 0

    answer = input("What keyword starts a condition? ").strip().lower()
    if answer == "if":
        score += 1

    answer = input("What operator compares equality? ").strip()
    if answer == "==":
        score += 1

    answer = input("True or False: else needs a condition. ").strip().lower()
    if answer == "false":
        score += 1

    print("Score:", score, "out of 3")

    if score == 3:
        print("Strong conditional thinking.")
    elif score == 2:
        print("Almost there.")
    else:
        print("Review if, elif, else, and comparison operators.")


def main():
    # Uncomment one example at a time.
    example_01_plain_if()
    # example_02_if_else()
    # example_03_comparison_operators()
    # example_04_if_elif_else()
    # example_05_order_matters()
    # example_06_boolean_and()
    # example_07_boolean_or()
    # example_08_boolean_not()
    # example_09_input_cleanup()
    # example_10_nested_if()
    # example_11_range_check()
    # example_12_membership_with_in()
    # example_13_common_bug_assignment_vs_comparison()
    # example_14_common_bug_indentation()
    # example_15_truthy_values()
    # example_16_mini_project_decision_helper()
    # example_17_challenge_simple_quiz()


if __name__ == "__main__":
    main()
