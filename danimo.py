# Spacing Functions

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

def spacing(lineBreaks, dashes):
    lines(lineBreaks)
    print("- " * dashes)
    lines(lineBreaks)

def spacing2(lineBreaks, char, repetition):
    lines(lineBreaks)
    print(f"{char} " * repetition)
    lines(lineBreaks)

# spacing2(2, "*", 16)
# spacing2(3, "/", 116)

# Turtle Functions

import turtle

# Function to set the color, speed & pensize of the next turtle as simple arguments:
def turSet(color, speed, pensize):
    turtle.color(color)
    turtle.speed(speed)
    turtle.pensize(pensize)
    turtle.shape("turtle")

# Function to move without markings:
def turMove(length):
    turtle.penup()
    turtle.forward(length)
    turtle.pendown()
