# Begin W2 D2 M4 Learning Activity:
# Writing Input/Output (I/O) Programs

print("")
print("LEARNING ACTIVITY : I/O : Q1")
print('')

movie = "'The Little Mermaid'"
myRating = 5
# yourRating = eval(input("On a scale of 1 to 5, how would you rate the movie", movie, "?"))
    # DOESN'T WORK requesting input combined with a variable
yourRating = eval(input("On a scale of 1 to 5, how would you rate the movie 'The Little Mermaid'? "))

print("")

if yourRating == 5:
    print("Wow, I love", movie, "too! We rate it exactly the same!")
elif yourRating > 3:
    print("Nice, I love", movie, "! Our ratings differ just a little, by", myRating - yourRating, ". Pretty neat!")
else:
    print("Oh no, I love", movie, "! Our ratings differ quite a bit, by", myRating - yourRating, ".")

