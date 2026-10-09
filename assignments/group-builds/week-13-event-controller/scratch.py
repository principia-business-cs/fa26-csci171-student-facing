import turtle
screen = turtle.Screen()
artist = turtle.Turtle()

def forward():
    artist.forward(20)

screen.onkey(forward, 'Up')
screen.listen()
turtle.done()
