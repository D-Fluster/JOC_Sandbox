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



