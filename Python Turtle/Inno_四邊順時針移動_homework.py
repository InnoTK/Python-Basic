import turtle
import random

window=turtle.Screen()
window.colormode(255)
window.setup(width=600, height=400)
window.tracer(0)

def 畫正方形(turtle1, length, color) :      #設定新函式"畫正方形" 開始

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
    return None                             #設定新函式"畫正方形" 完成

bob1=turtle.Turtle()                        
bob1.shape("classic")
bob1.speed(0)
bob1.hideturtle()
bob1.penup()
r1 = random.randint(100, 200)         #隨機方塊顏色               
g1 = random.randint(100, 200)               
b1 = random.randint(100, 200)

size=80
x=-window.window_width()/2+size/2   
y=window.window_height()/2-size/2
speed = 0.1                 #設定 移動"速度"
direction = "向右"          #設定 移動"方向"

while True:                 #無窮迴圈

    bob1.clear()            #清除上個圖案
    bob1.goto(x,y)           
    畫正方形(bob1, size,(r1,g1,b1))      #隨機方塊顏色
                                            #四邊順時移動 "控制" 開始
    
    if direction == "向右":                             #頂邊移動
        x += speed
        if x >= window.window_width()/2-size/2:     #轉向
            direction = "向下"
    elif direction == "向下":                           #右邊移動
        y -= speed
        if y <= -window.window_height()/2+size/2:   #轉向
            direction = "向左"
    elif direction == "向左":                           #底邊移動
        x -= speed
        if x <= -window.window_width()/2+size/2:    #轉向
            direction = "向上"
    elif direction == "向上":                           #左邊移動   可簡化 else :
        y += speed
        if y >= window.window_height()/2-size/2:    #轉向
            direction = "向右"                          
                                            #四邊順時移動 "控制" 結束

    window.update()         #圖形滯留


window.exitonclick()