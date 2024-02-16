# Practice Using Functions
# Q1: Poem Madlibs

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

lines(1)
print("USING FUNCTIONS PRACTICE : Q1 : Poem Madlibs")
lines(1)

noun = input("First, please enter a funny PLURAL NOUN: ")
adj = input("Next, please enter a silly ADJECTIVE: ")

print("Great! Here's your madlib poem:")
print(noun.title(), "are red; violets are blue...")
    # Can also use noun.capitalize()
    # In PyCharm, can start typing "noun." to see a full list of options!
print("Monty Python is", adj.lower() + ", so WOO HOO!")
    # Why didn't this work for me before? O.o