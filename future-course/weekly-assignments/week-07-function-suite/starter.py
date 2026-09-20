def add_tax(subtotal, rate):
    return subtotal + subtotal * rate


def main():
    print('Function Suite')
    print('Expected 10.8, got', add_tax(10, 0.08))


if __name__ == '__main__':
    main()
