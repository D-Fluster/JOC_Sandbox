# Danimo's Turtle Sandbox!

import turtle

# Set turtle preferences:
turtle.shape("turtle")
turtle.speed(7)
# turtle.color("pink")
# turtle.screensize(1.0, 1.0)

# Function library:

def turMove(length):          # Function to move without markings
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()

def turLn(length, penWid, color):        # Function to draw lines
    turtle.color(color)
    turtle.pensize(penWid)
    turtle.forward(length)

# sqLen = 0
def turSq(sideLen, penWid, color):       # Function to draw squares
    turtle.color(color)
    turtle.pensize(penWid)
    for i in range(4):
        turtle.forward(sideLen)
        turtle.right(90)
    # sqLen = sideLen

def turRec(sideLen, sideWid, penWid, color, speed):       # Function to draw rectangles
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(penWid)
    for i in range(2):
        turtle.forward(sideLen)
        turtle.right(90)
        turtle.forward(sideWid)
        turtle.right(90)

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
STEPS 1-5
# Step 1: Drawing lines
turLn(-222, 5, "purple")

# Steps 2-4: Drawing squares
turSq(55, 3, "pink")
turMove(77)
turSq(111, 7, "green")

# Step 5: Drawing rectangles
turRec(55, 111, 3, "red", 5)
'''

# Step 6: Drawing pictures

# turMove(-555)
#
# for px in "Hello world / This is me / Life should be / Fun for everyone":
#     turRec(99, 77, 3, "black", 0)
#     turMove(33)
#     turSq(55, 5, "pink")

# turtle.speed(1)

turPic(111, 222, 33)

turtle.Screen().exitonclick()
    # Must be at the END of the turtle code
    # Keeps the turtle screen active until the user closes it
    # Rather than directly after everything is run