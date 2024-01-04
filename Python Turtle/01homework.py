import turtle
import random
window = turtle.Screen()
window.colormode(255) #能夠顏色用RGB(X，X，X)表示加入
window.setup(width=400,height=800)
window.tracer(0)

r1=random.randint(0,255)  
g1=random.randint(0,255) 
b1=random.randint(0,255) 
r2=random.randint(0,255) 
g2=random.randint(0,255) 
b2=random.randint(0,255) 


bob1 =  turtle.Turtle()
bob1.shape("turtle") #更改形狀
bob1.shapesize(1,1,1) #更改大小
#bob1.color("red","red") #更改顏色(線色,物體色)
bob1.speed(0)

bob1.color((240,240,0),(240,240,0)) #黃色
bob1.penup()
bob1.begin_fill()
bob1.goto(-200,0)
bob1.pendown()
for n in range(4):
    bob1.forward(400)
    bob1.left(90)
bob1.end_fill()

bob1.color((133,27,241),(133,27,241)) #紫色
bob1.penup()
bob1.begin_fill()
bob1.setheading(270)
bob1.pendown()
for n in range(4):
    bob1.forward(400)
    bob1.left(90)
bob1.end_fill()
#以上是方塊

bob1.color("green","green") 
bob1.penup()
bob1.begin_fill()
bob1.goto(0,50)
bob1.setheading(0)
bob1.pendown()
bob1.circle(150)
bob1.end_fill()

bob1.color("green","green") #淺綠
bob1.penup()
bob1.begin_fill()
bob1.goto(0,-350)
bob1.setheading(0)
bob1.pendown()
bob1.circle(150)
bob1.end_fill()
#以上是圓

for m in range(10) :
    
    for n in range(14) :
        bob1.penup()
        bob1.goto(-190+30*n,390-m*40)
        bob1.setheading(0)
        bob1.color((133,27,241),(133,27,241)) 
        bob1.pendown()
        bob1.dot(15)
        bob1.penup()
        bob1.goto(-205+30*n,370-m*40)
        bob1.pendown()
        bob1.dot(15)
        bob1.penup()
        bob1.goto(-190+30*n,-10-m*40)
        bob1.setheading(0)
        bob1.color((240,240,0),(240,240,0)) 
        bob1.pendown()
        bob1.dot(15)
        bob1.penup()
        bob1.goto(-205+30*n,-30-m*40)
        bob1.pendown()
        bob1.dot(15)
#以上是點點


window.exitonclick()