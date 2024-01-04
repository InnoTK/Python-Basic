import turtle
import random

window = turtle.Screen()
window.colormode(255)
window.setup(width=560, height=560)

bob1=turtle.Turtle()
bob1.shape("classic")
bob1.speed(0)

y=random.randint(1,25)
r1 = random.randint(30, 255)             
g1 = random.randint(30, 255)            
b1 = random.randint(30, 255)             

for c in range(5):
    # r1 = random.randint(0, 255)             #這  綁   才   機   效
    # g1 = random.randint(0, 255)             #幾  在   會   顏   果
    # b1 = random.randint(0, 255)             #個  一   有   色   ！
    # bob1.color((r1,g1,b1),(r1,g1,b1))       #要  起   隨   的   ！   <----這行不能獨立！
    for a in range(5):
        x=c*5+a+1
        bob1.penup()
        bob1.goto(-170+a*110,170-c*110)
        bob1.setheading(90)
        bob1.pendown()
        if y==x:
            bob1.color((r1,g1,b1),(r1,g1,b1))
        else:
            bob1.color((r1-30,g1-30,b1-30),(r1-30,g1-30,b1-30))   # <==小於0將會出錯
        bob1.begin_fill()
        for b in range(4):
            bob1.forward(100)
            bob1.left(90)
        bob1.end_fill()
# x = random.randint(0,4)                     #隨機挑選一塊變為紅色
# y = random.randint(0,4)
# bob1.color("red","red")
# bob1.penup()
# bob1.goto(-170+x*110,170-y*110)
# bob1.setheading(90)
# bob1.pendown()
# bob1.begin_fill()
# for d in range(4):
#     bob1.forward(100)
#     bob1.left(90)
# bob1.end_fill()
bob1.hideturtle()
window.exitonclick()