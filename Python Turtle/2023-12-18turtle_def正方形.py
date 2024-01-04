import turtle
import random

window=turtle.Screen()
window.colormode(255)
window.setup(width=1200, height=600)

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(0)

size=200

def 畫正方形(turtle1, length, color) :
    turtle1.color(color)
    turtle1.penup()
    turtle1.setheading(270)
    for m in range(2):
        turtle1.forward(length/2)
        turtle1.left(90)
    turtle1.pendown()
    turtle1.begin_fill()
    for n in range(4):
        turtle1.forward(length)
        turtle1.left(90)
    turtle1.end_fill()
    return print("done")
for m in range(2):
    for n in range(2):
        bob1.penup()
        bob1.goto(window.window_width()/2-size/2-(window.window_width()-size)*n,window.window_height()/2-size/2-(window.window_height()-size)*m)
        bob1.pendown()
        r1 = random.randint(0, 255)              
        g1 = random.randint(0, 255)               
        b1 = random.randint(0, 255)              
        畫正方形(bob1, size,(r1,g1,b1))


window.exitonclick()