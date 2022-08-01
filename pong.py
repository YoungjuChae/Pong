# Author: Youngju Chae
# Text-Based Pong Game

# Import Necessary Modules
from turtle import Screen, Turtle 
from scoreboard import Scoreboard 
from paddle import Paddle
from ball import Ball
import time 

# Create necessary variables
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard() 

# Create paddle movement
screen.listen() 
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Play Game
game_on = True
while game_on: 
  screen.update() 
  ball.move()
  # Detect collision with wall (top and bottom) 
  if (ball.ycor() > 280) or (ball.ycor() < -280): 
    ball.bounce_y() 
  # Detect collision with paddle (distance )
  if (ball.distance(l_paddle) < 50 and ball.xcor() == -335 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() == 335 and ball.xcor() > 320):
    ball.bounce_x()
  # Detect right paddle missing and hit wall 
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.reset()
  # Detect left paddle missing and hit wall 
  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.reset()

screen.exitonclick()
