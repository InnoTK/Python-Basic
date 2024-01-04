import turtle

window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.speed(2)

pen.penup()
pen.goto(0,-100)
pen.pendown()
pen.circle(100)

pen.penup()
pen.goto(-80,-100)
pen.pendown()
pen.forward(160)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(160)
pen.left(90)
pen.forward(200)

window.exitonclick()