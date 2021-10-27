"""
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0
floor_two = 21

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  y = y + 5 # location of next floor
  floor = floor + 1
  rem = floor % 6
  if (rem > 2):  
    painter.color("blue")
  #draw the floor
  painter.pendown()
  painter.forward(50)
  if floor == floor_two:
    x += 60
    y -= 21*5 
    floor_two += 21

wn = trtl.Screen()
wn.mainloop()

"""

z = 10
for i in range(2, 30):
  z += 1
  while z > 15:
    z += 3