# Spacing Functions

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

def spacing(lineBreaks, dashes):
    lines(lineBreaks)
    print("- " * dashes)
    lines(lineBreaks)




# Turtle Functions

import turtle

turtle.shape("turtle")

# Function to set the color, speed & pensize of the next turtle as simple arguments:
def turSet(color, speed, pensize):
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(pensize)

# Function to move without markings:
def turMove(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
