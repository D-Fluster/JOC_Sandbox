from danimo import *

# NOT WORKING AS EXPECTED:
# from turtleSandbox import *
# danimo.turSign(111)
# import turtleSandbox
# danimo.turtleSandbox.turSign(111)

spacing(1, "*", 33)



# Initializing 3 turtles

danimo = turtle.Turtle()
danimo.shape("turtle")
danimo.color("pink")
# danimo.fillcolor("yellow")
    # Makes the fill of the turtle yellow (with a pink outline) but not the polygon...
danimo.pensize(5)
danimo.speed(0)
# danimo.turSet("pink", 3, 3)
    # Returns an AttributeError: 'Turtle' object has no attribute 'turSet'

carlitos = turtle.Turtle()
carlitos.shape("circle")
carlitos.color("purple")
carlitos.fillcolor("green")
carlitos.pensize(3)
carlitos.speed(0)
carlitos.penup()
carlitos.goto(-100, -100)
carlitos.pendown()

munequita = turtle.Turtle()
munequita.shape("arrow")
munequita.color("red")
munequita.fillcolor("orange")
munequita.pensize(2)
munequita.speed(0)
munequita.penup()
munequita.goto(100, 100)
munequita.pendown()


# Moving the turtles!

for i in range(11):
    # danimo.begin_fill()
    danimo.forward(111)
    danimo.right(99 + i)
    # danimo.end_fill()

for i in range(33):
    carlitos.forward(i**2)
    carlitos.left(22*i)

for i in range(55):
    munequita.backward(5*i)
    munequita.right(2**i)


turtle.Screen().exitonclick()