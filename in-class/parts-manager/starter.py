"""Parts Desk: implement the TODOs in checkpoint order."""


def read_positive_int(prompt):
    """Provided helper: invalid input returns None instead of crashing."""
    try:
        amount = int(input(prompt))
    except ValueError:
        print("Enter a positive whole number.")
        return None
    if amount <= 0:
        print("Enter a positive whole number.")
        return None
    return amount


class Part:
    def __init__(self, part_id, name, quantity, price):
        # TODO: store four instance attributes on self.
        pass

    def restock(self, amount):
        # TODO: validate, change quantity, and return success/failure.
        pass

    def use(self, amount):
        # TODO: reject requests that would make stock negative.
        pass


def find_part(parts, part_id):
    # TODO: loop through objects and return the matching object or None.
    pass


def show_parts(parts):
    # TODO: print a row per object and mark quantity < 5 as LOW STOCK.
    pass


def main():
    # TODO: create the three Part objects in a list before the menu loop.
    # TODO: build the menu and connect choices to functions/methods.
    print("Parts Desk - ready for your implementation")


if __name__ == "__main__":
    main()
