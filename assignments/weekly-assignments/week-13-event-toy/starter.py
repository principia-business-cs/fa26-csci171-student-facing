import turtle

screen = turtle.Screen()
artist = turtle.Turtle()


def move_forward():
    artist.forward(20)


# Add at least two more callback functions.

screen.onkey(move_forward, 'Up')
screen.listen()
turtle.done()
