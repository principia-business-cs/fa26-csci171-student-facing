import turtle

screen = turtle.Screen()
artist = turtle.Turtle()


def draw_badge(size, color):
    artist.pencolor(color)
    for side in range(4):
        artist.forward(size)
        artist.right(90)


draw_badge(80, 'blue')
turtle.done()
