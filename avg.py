# Average calculator based on real (float) user input

print()
print("Hello and welcome to the average calculator!")
print()
print("Today we're going to calculate the average (mean) of your most recent 10 quiz scores.")
print()
print("When prompted, please enter each score in turn. You may include up to 2 decimal places.")
print()

# valArray = []
#
# for i in range(1, 11):
#     valArray[i] = float(input("How did you do on the quiz #" + print(i) + "?"))

# val0 = float(input("How did you do on the FIRST test? "))
# val1 = float(input("How did you do on the SECOND test? "))
# val2 = float(input("How did you do on the THIRD test? "))
# val3 = float(input("How did you do on the FOURTH test? "))
# val4 = float(input("How did you do on the FIFTH test? "))
# val5 = float(input("How did you do on the SIXTH test? "))
# val6 = float(input("How did you do on the SEVENTH test? "))
# val7 = float(input("How did you do on the EIGHTH test? "))
# val8 = float(input("How did you do on the NINTH test? "))
# val9 = float(input("How did you do on the TENTH test? "))
#
# print()
# print("Your average score over the last 10 quizzes was:", (val0 + val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8 + val9)/10)


# yourArray = [val1, val2, num]
# print(yourArray)


'''
FROM STACK OVERFLOW:
You can use string formatting to insert the value of x in the string:
    sales = float(input("Please enter your sales from day {}".format(x)))
The current value of x will be inserted in the placeholder {}
'''

valArray = []

# for i in range(1, 11):
#     valArray[i] = float(input("What was your score on Quiz #{}? ".format(i)))
      # IndexError: list assignment index out of range


# After watching part of the solution video:

valTot = 0      # initializes the "total value" variable
# From video walkthrough: called an 'aggregator' variable
# Provides a neutral starting point for the particular problem at hand
# 0 is neeutral in terms of addition, while 1 would be neutral for multiplication

for i in range(10):
    val = float(input("Please enter one quiz score at a time: "))
    valTot += val

valAvg = (valTot/10)      # averages all "val" variables

print()
print("Your average score over the last 10 quizzes was:", valAvg)

# Plus it occurs to me that this method should use a lot less memory/RAM,
# since storing ALL values as an array is unnecessary to solve the average problem,
# which can easily be solved by keeping only 2 numbers in memory for any n numbers to be averaged