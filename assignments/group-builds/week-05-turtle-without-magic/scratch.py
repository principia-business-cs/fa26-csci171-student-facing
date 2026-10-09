import turtle
artist = turtle.Turtle()
artist.pensize(3)
artist.pencolor('blue')
for side in range(4):
    artist.forward(80)
    artist.right(90)
artist.penup(); artist.goto(120, 0); artist.pendown()
artist.fillcolor('gold')
artist.begin_fill(); artist.circle(40); artist.end_fill()
turtle.done()
