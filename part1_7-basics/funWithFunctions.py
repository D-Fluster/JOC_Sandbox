import math

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

lines(1)

'''
print("MATH FUN...CTIONS")
lines(1)

print(math.sqrt(25))
lines(1)

print(math.log10(100))
lines(1)

print(abs(-5))
lines(2)

from math import log10

print(log10(100))
lines(3)
'''

print("STRING FUN...CTIONS")
lines(1)

phrase = "find your Yoda"
print("The phrase is... '", phrase, "'!")
lines(1)

print("GUESS: 'FIND YOUR YODA'")
print("ANSWER: ")
print(phrase.upper())
lines(1)

print("GUESS: 'Find Your Yoda' or 'Find your Yoda'")
print("ANSWER: ")
print(phrase.title())
lines(1)

print("GUESS: '2'")
print("ANSWER: ")
print(phrase.count("o"))
lines(1)

print("GUESS: '11'?")
print("ANSWER: ")
print(phrase.lower().islower())
lines(1)

print("GUESS: '0'?")
print("ANSWER: ")
print(phrase.isdecimal())
