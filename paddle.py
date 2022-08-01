# Import Necessary Modules
from turtle import Turtle

# Create class
class Paddle(Turtle):
  # Create paddles
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(position)
  
  # Paddle movement (up)
  def go_up(self): 
    new_y = self.ycor() + 20
    if new_y < 280:
      self.goto(self.xcor(), new_y)
  # Paddle movement (down)
  def go_down(self): 
    new_y = self.ycor() - 20
    if new_y > -280:
      self.goto(self.xcor(), new_y)
  
