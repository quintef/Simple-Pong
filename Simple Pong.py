import turtle
#initializing a window using turle
wn = turtle.Screen() 
wn.title("PONG CLONE") 
wn.bgcolor("black")
wn.setup(width=800,height=600)
#stop window from updating, we manually update it to make it run slightly smoother
wn.tracer(0)

#score
score_a = 0
score_b = 0

#Left Paddle "A"
paddle_a = turtle.Turtle()
paddle_a.speed(0)# speed of animation, set to max 
paddle_a.shape("square")#default shape 20*20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len= 1)# stretching width by 5 (20*5)
paddle_a.penup()# dont draw lines when moving 
paddle_a.goto(-350,0) # location of paddle A

#Right Paddle "B"
paddle_b = turtle.Turtle()
paddle_b.speed(0)# speed of animation, set to max 
paddle_b.shape("square")#default shape 20*20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len= 1)# stretching width by 5 (20*5)
paddle_b.penup()# dont draw lines when moving 
paddle_b.goto(350,0) # location of paddle B

#Ball
ball = turtle.Turtle()
ball.speed(0)# speed of animation, set to max 
ball.shape("square")#default shape 20*20 pixels
ball.color("white")
ball.penup()# dont draw lines when moving 
ball.goto(0,0) # location of paddle B

#function creation for movement of left paddle "a"
def paddle_aUp():
    y = paddle_a.ycor()#returns the y coordinate of paddle a
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor()>= 360:
        paddle_a.sety(-330)

def paddle_aDown():
    y = paddle_a.ycor()
    y = y - 20 
    paddle_a.sety(y)
    if paddle_a.ycor()<= -360:
        paddle_a.sety(330)

#function creation for movement of left paddle "b"
def paddle_bUp():
    y = paddle_b.ycor()#returns the y coordinate of paddle a
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor()>= 360:
        paddle_b.sety(-330)

def paddle_bDown():
    y = paddle_b.ycor()
    y = y - 20 
    paddle_b.sety(y)
    if paddle_b.ycor()<= -360:
        paddle_b.sety(330)

#key board binding 
wn.listen()
wn.onkeypress(paddle_aUp, "w")
wn.onkeypress(paddle_aDown, "s")
wn.onkeypress(paddle_bUp, "Up")
wn.onkeypress(paddle_bDown, "Down")

#moving the ball 
ball.dx = .2 # number of pixels the ball moves
ball.dy = .2

#score tracker pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0 Player B: 0",align = "center",font = ("Courier", 24, "normal"))




#main game loop
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check top/bottom
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 #reverse the dirrection of ball

    elif (ball.ycor()< -290):
        ball.sety(-290)
        ball.dy *= -1

    #border check left/right
    

    if ball.xcor()>390:
            ball.goto(0,0)
            ball.dx *= -1 
            score_a += 1
            pen.clear()
            pen.write("player A: {} Player B: {}".format(score_a,score_b),align = "center",font = ("Courier", 24, "normal"))
    if ball.xcor()<-390:
            ball.goto(0,0)
            ball.dx *= -1 
            score_b += 1
            pen.clear()
            pen.write("player A: {} Player B: {}".format(score_a,score_b),align = "center",font = ("Courier", 24, "normal"))

    #paddle collision 
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor() < paddle_b.ycor() + 50) and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1 
        
    if ball.xcor() < -340 and ball.xcor()>-350 and (ball.ycor() < paddle_a.ycor() + 50) and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1 
    



    

