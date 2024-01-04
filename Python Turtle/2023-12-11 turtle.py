import turtle #載入turtle module
window = turtle.Screen() #Screen為turtle module內的函式 #將右邊的資料傳至左邊的變數
window.colormode(255)  
bob1 = turtle.Turtle()
bob2 = turtle.Turtle() #烏龜取名叫bob
bob1.shape("turtle")
bob2.shape("turtle")
bob1.shapesize(5,5,2)
bob2.shapesize(2,2,2)
bob1.color("royalblue4", "gold1")
bob2.color("#FF3030", (248,248,255)) #firebrick1 FF3030 RGB(255,48,48)/ghostwhite F8F8FF RGB(248,248,255)
bob1.forward(75)
bob2.backward(75)
# print(dir(window))
# print(dir(bob))    #dir可顯示(object)所有的功能

window.exitonclick()