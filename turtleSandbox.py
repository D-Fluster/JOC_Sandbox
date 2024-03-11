# Danimo's Turtle Sandbox!

import turtle

### Function library:

# Function to set the color, speed & pensize of the next turtle as simple arguments:
def turSet(color, speed, pensize):
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(pensize)

# Set turtle preferences:

turtle.shape("turtle")
# turtle.speed(7)
# turtle.color("pink")
# turtle.screensize(1.0, 1.0)

# Function to move without markings:
def turMove(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

# Function to draw lines:
def turLn(length):
    # turtle.color(color)
    # turtle.pensize(penWid)
    turtle.forward(length)

# Function to draw squares:
def turSq(sideLen):
    # turtle.color(color)
    # turtle.pensize(penWid)
    for i in range(4):
        turtle.forward(sideLen)
        turtle.right(90)
    # sqLen = sideLen

# Function to draw equilateral triangles of ^ (not V) shape:
def turTri(sideLen):
    for i in range(3):
        turtle.forward(sideLen)
        turtle.left(120)

# Function to draw "houses":
def turHouse(sideLen):
    turTri(sideLen)
    turSq(sideLen)

# Generalized square function to draw rectangles:
def turRec(sideLen, sideWid):
    # turtle.color(color)
    # turtle.speed(speed)
    # turtle.pensize(penWid)
    for i in range(2):
        turtle.forward(sideLen)
        turtle.right(90)
        turtle.forward(sideWid)
        turtle.right(90)

# Function to draw octagons:
def turOct(sideLen):
    for i in range(8):
        turtle.forward(sideLen)
        turtle.left(45)

# Function to draw stop signs using octagons & rectangles:
def turSign(sideLen):
    postFwd = (2/5) * sideLen       # Adjusted from (3/8) for mathematical center
    # print(postFwd)                # Used in testing
    postWidth = (1/5) * sideLen
    postHeight = 2 * sideLen
    turOct(sideLen)                 # Draws the "STOP"
    turtle.forward(postFwd)
    turRec(postWidth, postHeight)   # Draws the signpost
    turMove(sideLen*2)              # Moves turtle out of the way

# def turSign2(sideLen):
#     postFwd = (3/8) * sideLen
#     print(postFwd)
#     postWidth = (1/5) * sideLen
#     postHeight = 2 * sideLen
#     turOct(sideLen)                 # Draws the "STOP"
#     turtle.forward(postFwd)
#     turRec(postWidth, postHeight)   # Draws the signpost
#     # turMove(sideLen*2)              # Moves turtle out of the way
#
# varLen = 191
#
# turSet("pink",9, 3)
# turSign(varLen)
#
# moveAmt = (varLen*2) + (2/5)*(varLen)
# turMove(-moveAmt)
#
# turSet("blue", 9, 2)
# turSign2(varLen)

# Function to draw silly pictures using square & rectangle functions above:
def turPic(len, wid, play):
    for i in range(play):
        turSq(len, 5, "pink")
        turtle.right(123)
        turMove(len*2)
        turRec(len, wid, 3, "purple", 7)
        turtle.left(234)
        turMove(len/5)

'''
END OF IMPORTS & FUNCTIONS      # Use Ctrl + D to DUPLICATE lines!
END OF IMPORTS & FUNCTIONS
END OF IMPORTS & FUNCTIONS
END OF IMPORTS & FUNCTIONS
END OF IMPORTS & FUNCTIONS
END OF IMPORTS & FUNCTIONS
'''

'''
STEPS 1-5:
----------
# Step 1: Drawing lines
turLn(-222, 5, "purple")

# Steps 2-4: Drawing squares
turSq(55, 3, "pink")
turMove(77)
turSq(111, 7, "green")

# Step 5: Drawing rectangles
turRec(55, 111, 3, "red", 5)

STEP 6:
-------
# Step 6: Drawing pictures

turMove(-555)
for px in "Hello world / This is me / Life should be / Fun for everyone":
    turRec(99, 77, 3, "black", 0)
    turMove(33)
    turSq(55, 5, "pink")
turtle.speed(1)

turPic(111, 222, 33)

STEP 7:
-------
# STEP 7: "house.py": Drawing a picture with functions

turTri(555)
turHouse(77)

STEP 8:
-------
# STEP 8: "stop.py": Drawing stop signs with functions

turSet("pink",9, 3)
turSign(111)
turSet("purple", 9, 2)
turSign(77)



# Chris Discord:
# def spiral(len,angle):
#     for i in range(len):            # Prints nothing with range(len, 10, 5)
#         turtle.forward(len)
#         turtle.right(angle)
#
# spiral(50,25)

# turOct(55)
'''


# # Discord @aaldwell 3/2/24
#
# def spiral(len, angle, spiralness):
#   variable_len = len
#   while variable_len > 1:
#     for i in range(2):
#       turtle.forward(variable_len)
#       turtle.right(angle)
#     variable_len /= spiralness
#
# spiral(111, 22, 1.11)



# # Discord Adam Armstrong (@rhianu) 3/10/24
# turtle.speed(0)
# turtle.Screen().setup(width=650, height=500)
# turtle.Screen().bgcolor("blue")
# turtle.color("white")
#
# radius = 30
#
# # turtle.speed(1)
# turtle.pensize(7)
#
# turtle.goto(205, 25)
# turtle.circle(radius)
#
# turtle.goto(70, 70)
# turtle.circle(radius)
#
# turtle.goto(250, -200)
# turtle.circle(radius)
#
# turtle.goto(0, 0)
# turtle.circle(radius)
#
# # Drawing circles using a loop:
# for i in range(1, 11):
#   turtle.circle(15 * i)
#
# # Modified version to move down first:
# turtle.goto(0, -200)
#
# for i in range(1, 11):
#   turtle.circle(15 * i)
#
# # Draw a solid triangle:
# turtle.Screen().bgcolor("blue")
# turtle.shape("turtle")
# turtle.color("green")
# # turtle.speed(0)
#
# size = 200
# turtle.penup()
# turtle.goto(-200, 200)
# turtle.pendown()
#
# def triangle(size):
#   for i in range(3):
#     turtle.forward(size)
#     turtle.right(120)
#
# for i in range(500):
#   triangle(5 + i)



turtle.Screen().exitonclick()
    # Must be at the END of the turtle code
    # Keeps the turtle screen active until the user closes it
    # Rather than directly after everything is run
