# Import Necessary Modules
from turtle import Turtle

# Create class
class Ball(Turtle):
  # Create pong ball
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.goto(0, 0)
    self.xmove = 0.5
    self.ymove = 0.5
    self.move_speed = 0.1
    
  # Determine ball location
  def move(self):
    new_x = self.xcor() + self.xmove
    new_y = self.ycor() + self.ymove
    self.goto(new_x, new_y)

# Bounce (up and down)
  def bounce_y(self):
    self.ymove *= -1
   
# Bounce (left and right)
  def bounce_x(self):
    self.xmove *= -1

# Reset ball position 
  def reset(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.bounce_x()
    
