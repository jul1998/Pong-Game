import time
from turtle import Turtle as T, Screen
from paddle import Paddle
from ball import Ball
from score import Score

#Set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
delay = 0.1 #Determine ball speed

#Create right and left paddle
r_paddle = Paddle(380,0)
l_paddle = Paddle(-380,0)

#Creates ball
ball = Ball()

#Creates score
score = Score()

#Controll paddles
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

#Listen keys
screen.listen()

#Main loop for game
game_on = True
while game_on:
    screen.update() # Avoid animation and update every iteration
    time.sleep(delay) # This will control ball speed
    ball.move_ball() # Move ball around
    score.paddle_scores() # Makes appear scores

    if ball.ycor() > 280 or ball.ycor() < -280: # Makes ball bounce whenever reaches top or bottom
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 370: # Ball detect collision  with right paddle and increases speed
        ball.colission_with_r_paddle()
        delay *= 0.8

    if ball.distance(l_paddle) < 50 and ball.xcor() < -340: #Ball detect collision  with left paddle and increases speed
        ball.colission_with_l_paddle()
        delay *= 0.8

    if ball.xcor() > 390: # Whenever ball passes the right paddle, reset ball position and speed, and update left paddle score
        ball.reset_ball()
        score.update_l_paddle_score()
        delay = 0.1


    if ball.xcor() < -390: # Whenever ball passes the left paddle, reset ball position and speed, and update right paddle score
        ball.reset_ball()
        score.update_r_paddle_score()
        delay = 0.1
    print(delay)









screen.exitonclick()
