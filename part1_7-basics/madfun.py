# Practice Using Functions
# Q2: Rounding & Absolute Values

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

import math

lines(1)
print("USING FUNCTIONS PRACTICE : Q2 : Rounding & Absolute Values")
lines(1)

num = float(input("Pick a number, any number: "))
lines(1)

print("Cool, here are some fun facts about", num, "!")
print("(1) The absolute value of", num, "is", abs(num), "...")
print("(2) Rounded to the nearest whole number,", num, "is", round(num), "... and, last but not least...")
print("(3) The square root of the absolute value of", round(num), "is", math.sqrt(abs(round(num))), "!")
    # Can add a second argument to the "round" function which specifies the number of decimal points to round to
    # e.g., for round(float, 2) to round to 2 decimal places
    # NOTE: doesn't seem to work for numebrs with fewer decimal places, e.g. round (5, 2) = 5, NOT 5.00
    # print(round(5.3848594, 2))  # = 5.38