#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.color(new_color)
  t.penup()
  my_turtles.append(t)

#  Setting the initilal position of the turtle
startx = 0
starty = 0

# iterating over each turtle and moving the turtle for each value in my_turtle
direction = 90

for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)     
  t.forward(50)

  direction = t.heading()

#	Updating the starting x and y values
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()