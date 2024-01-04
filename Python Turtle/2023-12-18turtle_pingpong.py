from turtle import Turtle, Screen, Shape   #從turtle Module 載入這三種class

# Screen
screen = Screen()
screen.setup(600, 400)   # width, height

# Playing field boundaries 遊戲範圍 長方形4頂點座標
play_top    = screen.window_height() / 2 - 100    # top of screen minus 100 units  Y值
play_bottom = -screen.window_height() / 2 + 100   # 100 from bottom                Y值
play_left   = -screen.window_width() / 2 + 50     # 50 from left                   X值
play_right  = screen.window_width() / 2 - 50      # 50 from right                  X值

# 遊戲範圍
area = Turtle()
area.hideturtle()
area.penup()
area.goto(play_right, play_top)
area.pendown()
area.goto(play_left, play_top)
area.goto(play_left, play_bottom)
area.goto(play_right, play_bottom)
area.goto(play_right, play_top)

# Ball
ball = Turtle()
ball.penup()
ball.shape("circle")        # Use the built-in shape "circle"
ball.shapesize(0.5, 0.5)   # Stretch it to half default size
ball_radius = 10 * 0.5      # Save the new radius for later

# 板子
L = Turtle()
R = Turtle()
L.penup()
R.penup()

# 板子外型
paddle_w_half = 10 / 2      # 10 units wide
paddle_h_half = 40 / 2      # 40 units high
paddle_shape = Shape("compound")  #為turtle設定新外型
paddle_points = ((-paddle_h_half, -paddle_w_half),
                 (-paddle_h_half, paddle_w_half),
                 (paddle_h_half, paddle_w_half),
                 (paddle_h_half, -paddle_w_half))
paddle_shape.addcomponent(paddle_points, "yellow","blue")
screen.register_shape("板子", paddle_shape)  #註冊 paddle_shape名字為板子
            # poly = ((0,0),(10,-5),(0,10),(-10,-5))
            # s = Shape("compound")
            # s.addcomponent(poly, "red", "blue")
            # screen.register_shape("亂畫",s)
L.shape("板子")
R.shape("板子")
            
#設定板子到 starting position
L.setx(play_left + 10)
R.setx(play_right - 10)

# Score
score_turtle = Turtle()
score_turtle.penup()
score_turtle.hideturtle()

score_L = 0
score_R = 0

def write_scores() :
    score_turtle.clear()
    score_turtle.goto(-screen.window_width()/4, screen.window_height()/2 - 80)
    score_turtle.write(score_L, align="center", font=("Arial", 32, "bold"))
    score_turtle.goto(screen.window_width()/4, screen.window_height()/2 - 80)
    score_turtle.write(score_R, align="center", font=("Arial", 32, "bold"))

write_scores()


screen.exitonclick()