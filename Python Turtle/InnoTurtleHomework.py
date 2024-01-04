import turtle
import time

window = turtle.Screen()
window.colormode(255)
window.setup(width=1200, height=600)
window.tracer(0)

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(0)

bob1.penup()           #底色開始
bob1.goto(0,-300)
bob1.pendown()
bob1.color("red","red")
bob1.begin_fill()
for n in range(4):
    bob1.left(90)
    bob1.forward(600)
bob1.end_fill()
bob1.color("green","green")
bob1.begin_fill()
for n in range(4):
    bob1.forward(600)
    bob1.left(90)
bob1.end_fill()        #底色結束


for n in range(2):         #2大圓開始
    bob1.penup()           
    bob1.goto(-300+n*600,-150)
    bob1.pendown()
    bob1.color("magenta","magenta")
    bob1.begin_fill()
    bob1.circle(150)
    bob1.end_fill()        #2大圓結束


for n in range(24):            #點點開始
    for m in range(24):
        bob1.penup()
        bob1.goto(-585+m*50,285-n*25)
        bob1.setheading(270)
        bob1.pendown()
        if m<=11:
            bob1.dot(15,'green')
        else:
            bob1.dot(15,'red')
            
for n in range(24):
    for m in range(23):
        bob1.penup()
        bob1.goto(-560+m*50,270-n*25)
        bob1.setheading(270)
        bob1.pendown()
        if m<=11:
            bob1.dot(15,'green') 
        else:
            bob1.dot(15,'red')  #點點結束

bob1.hideturtle()
window.exitonclick()