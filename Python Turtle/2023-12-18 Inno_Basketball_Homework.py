import turtle
import random

window=turtle.Screen()
window.colormode(255)
window.setup(width=800, height=600)
window.tracer(0)
def 畫圓形(t1, r, color01) :
    t1.color(color01)
    t1.penup()
    t1.forward(r)
    t1.setheading(90)
    t1.pendown()
    t1.begin_fill()
    t1.circle(r,360)
    t1.end_fill()
    t1.penup()

# def 畫正方形(turtle1, length, color02) :
#     turtle1.color(color02)
#     turtle1.penup()
#     turtle1.setheading(270)
#     for m in range(2):
#         turtle1.forward(length/2)
#         turtle1.left(90)
#     turtle1.pendown()
#     turtle1.begin_fill()
#     for n in range(4):
#         turtle1.forward(length)
#         turtle1.left(90)
#     turtle1.end_fill()
#     turtle1.penup()
#     return print("done")

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(0)
bob1.hideturtle()
bob1.penup()
size=50
x=-window.window_width()/2+size   #-275
y=window.window_height()/2-size
dx=0.3      #每次移動0.1
dy=0.3
while True: #無窮迴圈
    bob1.clear()
    bob1.goto(x,y)
    r1 = random.randint(0, 255)              
    g1 = random.randint(0, 255)               
    b1 = random.randint(0, 255)              
    畫圓形(bob1, size,(r1,g1,b1))


    if x>window.window_width()/2:
        dx = -dx
    elif x<-window.window_width()/2+1.5*size:    #-275
        dx = -dx
    x += dx

    if y>window.window_height()/2-1.5*size:
        dy = -dy
    elif y<-window.window_height()/2:    #-175
        dy = -dy
    y += dy

    window.update()  #圖形滯留


window.exitonclick()