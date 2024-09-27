from main import Txrtle
import turtle as trtl

my_turtles = []
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
startx = 0
starty = 0
direction = 90

bbg = Txrtle(turtle_shapes,turtle_colors,my_turtles, startx, starty, direction)
bbg.setShapeColor()
bbg.move_turtle()
print(bbg.__str__())

trtl.done()