#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()

painter.speed(0)
painter.shape("circle")
painter.hideturtle()
painter.penup()

y = -200
while (y < 200): 
  x = -200
  y += 50
  painter.goto(x,y)
  painter.color("purple")
  painter.stamp()

  while (x < 100):
    x += 50
    painter.goto(x,y)
    painter.color("orange")
    painter.stamp() 


wn = trtl.Screen()
wn.mainloop()