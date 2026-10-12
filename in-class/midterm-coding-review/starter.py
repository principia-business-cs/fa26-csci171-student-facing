def attendance_message(days_present, total_days):
    # TODO: Return excellent attendance, steady attendance, or needs a plan.
    return "TODO"


def count_scores_at_least(scores, target):
    # TODO: Count how many scores are greater than or equal to target.
    return 0


def build_inventory_value(items):
    # TODO: Build a dictionary where each item maps to price * quantity.
    inventory_values = {}
    return inventory_values


def average(values):
    # TODO: Return the average of the values list.
    return 0


def print_club_summary(club_hours):
    # TODO: Print each club's average and whether it is on track or needs check in.
    for club_name, hours in club_hours.items():
        print(f"{club_name} average: {average(hours)} - TODO")


def main():
    print("Problem 1")
    print(attendance_message(18, 20))
    print(attendance_message(15, 20))
    print(attendance_message(10, 20))

    print("\nProblem 2")
    print(count_scores_at_least([82, 91, 77, 100, 88], 85))
    print(count_scores_at_least([70, 72, 74], 75))

    print("\nProblem 3")
    inventory = [
        ("notebook", 2.50, 4),
        ("pen", 1.25, 10),
        ("folder", 3.00, 2),
    ]
    print(build_inventory_value(inventory))

    print("\nProblem 4")
    club_hours = {
        "Robotics": [3, 4, 3],
        "Chess": [2, 2, 3],
        "Choir": [4, 4, 5],
    }
    print_club_summary(club_hours)


if __name__ == "__main__":
    main()
