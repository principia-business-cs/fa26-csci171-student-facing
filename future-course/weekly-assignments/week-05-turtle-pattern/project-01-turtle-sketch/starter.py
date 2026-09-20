import turtle


def draw_square(artist, size):
    for side in range(4):
        artist.forward(size)
        artist.right(90)


def main():
    artist = turtle.Turtle()
    draw_square(artist, 80)
    turtle.done()


if __name__ == '__main__':
    main()
