"""
8/6/2018
From How to Think Like a Computer Scientist, "Turtles" chapter
Gives you a module with a window and cursor which draws according to code
and parameters based on user input. This version prints a grid of 16 circles
of uniform size with different colors for each row.
I wanted to make it scalable and flexible
according to input; maybe I'll expand later.
"""

import turtle
wn = turtle.Screen()
tess = turtle.Turtle() # making a "turtle" called Tess

# Getting user input for Tess
print("Set the parameters:")
screen_color = input("Background color")
print("""Input a 4-digit code to set the color of
each row in order in the format xxxx.

0 = Black
1 = Red
2 = Blue
3 = Green
4 = Yellow
5 = Gray
6 = White
7 = Purple
8 = Orange
9 = Brown""")

# Getting user input for pen color and thickness, converting to int
tess_colors_str = input("Input 4-digit color code for Tess here")
tess_pen_str = input("Thickness for Tessie's Tail")
tess_pen_int = int(tess_pen_str)

# Holding available colors in dictionary for variables 0-9
colorlist = [
  "Black",
  "Red",
  "Blue",
  "Green",
  "Yellow",
  "Gray",
  "White",
  "Purple",
  "Orange",
  "Brown"
  ]

wn.bgcolor(screen_color)        # set the window background color
tess.pensize(tess_pen_int)          # set the width of Tess' pen

#setting initial position
tess.up()
tess.left(90)
tess.forward(114)
tess.left(90)
tess.forward(114)
tess.right(90)
tess.down()

"""
Drawing 16x16 bubble grid
Tess' direction alternates with each bubb
The overall direction reverses each row
This is to avoid imprecise math
math is hard
"""

rowcount = 0             # counting rows up to 4
while rowcount <= 3:
  newcolor = tess_colors_str[rowcount] # Figuring out which color by row
  newcolor_int = int(newcolor)    # Making color code int for index
  tess.color(colorlist[newcolor_int]) # Setting Tess's color for this row

  if rowcount % 2 == 0: # Even rows go left to right
    if rowcount == 2:
      tess.up()
      tess.forward(58)
      tess.right(180)
      tess.down()
    bubblerow = 0          # counting bubbles in a row up to 4
    while bubblerow <= 3:
      if bubblerow % 2 == 0:
        count = 0            # counting pixels
        while count <= 269:
          if count == 180:
            tess.up()
          tess.forward(1)
          tess.right(2)
          count += 1
        tess.down()
        bubblerow += 1
      else:
        count = 0            # counting pixels
        while count <= 269:
          if count == 180:
            tess.up()
          tess.forward(1)
          tess.left(2)
          count += 1
        tess.down()
        bubblerow += 1
    rowcount += 1
  else:
    #moving Tess to new row beginning
    tess.up()
    tess.right(180)
    tess.forward(57)
    tess.down()

    bubblerow = 0          # counting bubbles in a row up to 4
    while bubblerow <= 3:
      if bubblerow % 2 == 0:
        count = 0            # counting pixels
        while count <= 269:
          if count == 180:
            tess.up()
          tess.forward(1)
          tess.right(2)
          count += 1
        tess.down()
        bubblerow += 1
      else:
        count = 0            # counting pixels
        while count <= 269:
          if count == 180:
            tess.up()
          tess.forward(1)
          tess.left(2)
          count += 1
        bubblerow += 1
      tess.down()
    rowcount += 1



wn.exitonclick()                # wait for a user click on the canvas
