import turtle

artist = turtle.Turtle()
artist.speed(6)
artist.pencolor("blue")

for side in range(4):
    artist.forward(80)
    artist.right(90)

artist.penup()
artist.forward(120)
artist.pendown()
artist.circle(40)

turtle.done()
