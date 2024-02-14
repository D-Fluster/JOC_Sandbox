import danimo
danimo.spacing2(1, "=", 22)



'''
title1 = "23.code/file_read_simple.py"
print(title1)
danimo.spacing2(0,".", len(title1)//2 + 1)

addFileTest = open("week3_add.txt", "r")
print(addFileTest.read())
addFileTest.close()
danimo.spacing2(1, "=", 22)



title2 = "23.code/file_write.py"
print(title2)
danimo.spacing2(0,".", len(title2)//2 + 1)

prompt = "Please enter the NEXT LINE you'd like to write into this file: "
user_file = input("Please enter a NAME for your file: ")
user_file_lines = int(input("How many LINES will your new file contain? "))

new_file = open(user_file, "w")

for i in range(user_file_lines):
    user_input = input(prompt)
    print(user_input, file = new_file)

new_file.close()



# Day 5
# Writing Files Practice
# Q1

adding_dashes = open("HelloWorld", "r")

for line in adding_dashes:
    print(f"- {line}")



# Q2

user_file_nums = input("Please enter a NAME for your file: ")
new_file_nums = open(user_file_nums, "w")

prompt_nums = "Please enter an integer value (or type '0' to exit): "
user_input_nums = input(prompt_nums)

while int(user_input_nums) != 0:
    print(user_input_nums, file=new_file_nums)
    user_input_nums = input(prompt_nums)

new_file_nums.close()


# BUT WHY DOESN'T THIS WORK?!

userFile_nums = input("Please enter a NAME for your file: ")
newFile_nums = open(userFile_nums, "w")

prompt_nums = "Please enter an integer value (or type '0' to exit): "
userInput_nums = input(prompt_nums)
userInputInt_nums = int(input(prompt_nums))

while userInputInt_nums != 0:
    print(userInputInt_nums, file = newFile_nums)
    userInputInt_nums = int(input(prompt_nums))

newFile_nums.close()

# ThisIsOnlyATxt
# ThisIsOnlyATest.txt

# user_input = input(prompt_num)



# Q3 & Q4

# # This works!
# TestINK = open("TestINK", "r")
# print(TestINK.read())

# stringy = "Hello there mister man and little lady! What's up this fine Friday?"
# print(stringy.split())              # ['Hello', 'there', 'mister', 'man', 'and', 'little', 'lady!', "What's", 'up', 'this', 'fine', 'Friday?']
# print(stringy.split("!"))           # ['Hello there mister man and little lady', " What's up this fine Friday?"]

def fileLineCount(fileName):
    fileName = open(fileName, "r")
    numLines = 0
    for line in fileName:
        numLines += 1
    return numLines

def fileWordCount(fileName):
    fileName = open(fileName, "r")
    numWords = 0
    for line in fileName:
        numWords += len(line.split())
    return numWords

countFiles = ["week3_text1.txt", "week3_text2.txt", "week3_text3.txt"]

countLines_results = []
for i in range(len(countFiles)):
    countLines_results.append(fileLineCount(countFiles[i]))
# print(countLines_results)         # [4, 3, 2] as expected

countWords_results = []
for i in range(len(countFiles)):
    countWords_results.append(fileWordCount(countFiles[i]))
# print(countWords_results)         # [8, 6, 4] as expected

# Is there a way to create this string through a loop and then pass it back to print?

outputFile = open("count.txt", "w")
outputFile.write(f"File {countFiles[0]} has {countLines_results[0]} lines \n"
                 f"File {countFiles[1]} has {countLines_results[1]} lines \n"
                 f"File {countFiles[2]} has {countLines_results[2]} lines")

outputFile = open("counts.txt", "w")
outputFile.write(f"File {countFiles[0]} has {countLines_results[0]} lines and {countWords_results[0]} words \n"
                 f"File {countFiles[1]} has {countLines_results[1]} lines and {countWords_results[1]} words \n"
                 f"File {countFiles[2]} has {countLines_results[2]} lines and {countWords_results[2]} words \n"
                 f"In total, all {len(countFiles)} files have {sum(countLines_results)} lines and {sum(countWords_results)} words")



# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(",.qsw")
# print(x)        # banana
# 
# trying = "ajcl;eakj;lceajl;kjcejl;acu ea;j jn f  ljceal;k  HELLO jelj;coiuo e"
# print(trying.strip("ajcl;ku nfiu"))     # eakj;lceajl;kjcejl;acu ea;j jn f  ljceal;k  HELLO jelj;coiuo e
'''



title3 = "Sample Grades Data Project"
print(title3)
danimo.spacing2(0,".", len(title3)//2 + 1)


# import pandas
# sampleGrades = pandas.read_csv('week3_sample-grades.csv', index_col='Name')
# # ERRORS

import csv

from statistics import stdev

# sampleGrades = csv.reader("week3_sample-grades.csv")
# print(sampleGrades)
# # Just outputs: <_csv.reader object at 0x000001F0D92391E0>

def meanList(list):
    return round(sum(list) / len(list), 2)

def medianList(list):
    list.sort()
    # print(list)           # Works throughout function properly
    if len(list)%2 == 1:
        med = ((len(list) + 1) // 2) - 1
            # When a list has an odd number of entries, the median value is the middlemost --
            # e.g., for a 5-entry list with index 1 to n, it's in position (5+1)/2
        # print(med)           # Works as expected!
        return list[med]
    else:                       # i.e., if len(list)%2 == 0:
        med = len(list) // 2
        # med2 = med1 + 1
            # For lists with an even number of entries, the median is the mean value of the
            # two middlemost entries (i.e., the one at half of len(list) and the next one
        # print([list[med - 1], list[med]])     # Works as expected!
        return meanList([list[med - 1], list[med]])

# print(medianList([1, 2, 3, 4, 5]))          # Odd len test case
#                                             # Returns 3 as expected
# print(medianList([1, 2, 3, 4, 5, 6]))       # Even len test case
#                                             # Returns 3.5 as expected

# Tab & shift-tab to indent & de-dent blocks!

with open("week3_sample-grades.csv") as csvfile:
    sampleGrades = csv.reader(csvfile)
    fallGrades = []
    springGrades = []
    for row in sampleGrades:
        if row[1] == "Fall 2016":
            fallGrades.append(int(row[2]))
        elif row[1] == "Spring 2016":               # Being explicit here in case other semesters are later compared (irl)
            springGrades.append(int(row[2]))

    fallGrades.sort()
    springGrades.sort()

    print(f"Fall grades sorted: {fallGrades}")
    print(f"Spring grades sorted: {springGrades}")
    danimo.spacing2(1, "*", 33)

    print(f"Fall mean grade: {meanList(fallGrades)}")
    print(f"Spring mean grade: {meanList(springGrades)}")
    danimo.spacing2(1, "*", 33)

    print(f"Fall median grade: {medianList(fallGrades)}")
    print(f"Spring median grade: {medianList(springGrades)}")
    danimo.spacing2(1, "*", 33)

    print(f"Fall standard deviation: {round(stdev(fallGrades), 2)}")
    print(f"Spring standard deviation: {round(stdev(springGrades), 2)}")
        # Values differ slightly from expected output:
        # Fall act 6.41 vs exp 6.29
        # Spr act 10.41 vs exp 10.17
        # Likely due to the preciseness of the imported function versus a created one
        # Yes, verified using Excel =stdev(vals)!

    # print(", ".join(col))           # Prints as comma-separated lines, rather than sets



