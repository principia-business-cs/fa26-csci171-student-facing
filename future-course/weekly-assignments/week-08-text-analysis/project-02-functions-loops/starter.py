import turtle


def make_artist():
    artist = turtle.Turtle()
    artist.speed(0)
    return artist


def main():
    artist = make_artist()
    # Build your visual pattern here using functions and loops.
    turtle.done()


if __name__ == '__main__':
    main()
