
import turtle as trtl

class Txrtle():
  def __init__(self,shapes,colors,my_turtles,startx,starty, direction):
    self.shapes = shapes
    self.colors = colors
    self.turtles = my_turtles
    self.sx = startx
    self.sy = starty
    self.direction = direction

  def setShapeColor(self):
    for s in self.shapes:
      t = trtl.Turtle(shape=s)
      new_color = self.colors.pop()
      t.color(new_color)
      t.penup()
      self.turtles.append(t)

  def move_turtle(self):
    for t in self.turtles:
      t.goto(self.sx, self.sy)
      t.pendown()
      t.setheading(self.direction)
      t.right(45)     
      t.forward(50)

      self.direction = t.heading()

      self.sx = t.xcor()
      self.sy = t.ycor()

  def __str__(self):
    return f"Turtle Shapes: {self.shapes}"