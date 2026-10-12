def shipping_zone(distance_miles):
    # TODO: Return local, regional, national, or long distance.
    return "TODO"


def first_long_name(names):
    # TODO: Return the first name longer than 6 characters, or none found.
    return "TODO"


def build_letter_counts(words):
    # TODO: Build and return a dictionary where each word maps to its length.
    letter_counts = {}
    return letter_counts


def average(scores):
    # TODO: Return the average of the scores list.
    return 0


def print_team_report(team_scores):
    # TODO: Loop through team_scores.items() and print each team's average.
    for team_name, scores in team_scores.items():
        print(f"{team_name} average: {average(scores)}")


def main():
    print("Problem 1")
    print(shipping_zone(10))
    print(shipping_zone(25))
    print(shipping_zone(120))
    print(shipping_zone(700))

    print("\nProblem 2")
    print(first_long_name(("Ana", "Bo", "Caroline", "Dee")))
    print(first_long_name(("Mia", "Noor", "Kai")))

    print("\nProblem 3")
    word_lengths = build_letter_counts(["sun", "moon", "stars"])
    print(word_lengths)

    print("\nProblem 4")
    team_scores = {
        "Blue": [9, 8, 9],
        "Gold": [7, 8, 7],
        "Green": [10, 9, 8],
    }
    print_team_report(team_scores)


if __name__ == "__main__":
    main()
