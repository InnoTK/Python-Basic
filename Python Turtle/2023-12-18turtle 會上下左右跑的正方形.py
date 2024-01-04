import turtle
import random

window=turtle.Screen()
window.colormode(255)
window.setup(width=600, height=400)
window.tracer(0)
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
    turtle1.penup()
    return print("done")

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(0)
bob1.hideturtle()
bob1.penup()
size=50
x=-window.window_width()/2+size/2   #-275
y=window.window_height()/2-size/2
dx=0.1      #每次移動0.1
dy=0.1
while True: #無窮迴圈
    bob1.clear()
    bob1.goto(x,y)
    r1 = random.randint(0, 255)              
    g1 = random.randint(0, 255)               
    b1 = random.randint(0, 255)              
    畫正方形(bob1, size,(r1,g1,b1))


    if x>window.window_width()/2-size/2:
        dx = -dx
    elif x<-window.window_width()/2+size/2:    #-275
        dx = -dx
    x += dx

    if y>window.window_height()/2-size/2:
        dy = -dy
    elif y<-window.window_height()/2+size/2:    #-175
        dy = -dy
    y += dy

    window.update()  #圖形滯留


window.exitonclick()