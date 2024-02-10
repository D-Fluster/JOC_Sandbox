# Begin W2 D2 M4 Learning Activity:
# Writing Input/Output (I/O) Programs

def lines(numBreaks):
    for i in range(numBreaks):
        print()       # or the empty string print("")

lines(1)




# for i in "howdy".upper():
#    print("howdy", end="!! ")

saying = "howdy"
for u in saying.upper():
# "saying.upper()" = "HOWDY" = still a 5-character string
   print(saying, end="!! ")
   print()
   # print(saying.upper())

'''

for int in range(1, 6):
   print(int)
lines(1)

for val in range(2, 12, 3):
   print(val)
lines(1)

for num in range(-10, 1, 2):
   print(num, end=" ")
lines(2)

for i in range(4):
   print("****")
lines(1)

# newList = []
#
# for num in range(-10, 1, 2):
#    newList(num) = num
#
# print(newList)

for char in "CSCI 150":
   print(char)
lines(1)

for num in range(1, 11):
   print(num)
lines(1)

for num in range(10, 26, 5):
   print(num, end=" ")
lines(2)        # extra line break needed when print isn't adding one

for i in range(-3, 22, 3):
   print(i, end=", ")
lines(2)

# BUT this will have a comma after the final number! Hmm... While not scalable *and* not all on one line, this particular problem *could* be solved by instead using:

for i in range (-3, 21, 3):
   print(i, end=", ")
print("21")
lines(2)

'''