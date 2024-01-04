import turtle

turtle.setup(600,600)

turtle.penup()
turtle.goto(-250,150)
turtle.pendown()
turtle.color("red")
turtle.speed(0)
turtle.begin_fill()
for n in range(2):
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-250,150)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
for n in range(2):
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-175,75)
turtle.pendown()
turtle.color("white")
turtle.right(15)
turtle.begin_fill()
for n in range(12):
    turtle.forward(90)
    turtle.left(150)
turtle.end_fill()

turtle.penup()
turtle.goto(-154,75)
turtle.pendown()
turtle.width(4)
turtle.color("blue")
turtle.setheading(270)
turtle.circle(26)

turtle.exitonclick()