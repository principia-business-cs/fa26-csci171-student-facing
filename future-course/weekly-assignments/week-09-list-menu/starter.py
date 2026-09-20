def display_items(items):
    for item in items:
        print('-', item)


def main():
    items = ['read', 'practice']
    choice = ''
    while choice != 'q':
        print('a add | r remove | d display | q quit')
        choice = input('Choose: ').strip().lower()
        # Add menu branches here.


if __name__ == '__main__':
    main()
