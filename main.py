# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import danimo

danimo.spacing(1, "~ ", 22)
print("Oops, you just ran 'main.py' but you didn't mean to, did ya? ;D")
danimo.spacing(1, "~ ", 22)


# punc = '! () – [] {} : ; \ , <> . / ? @ # $ % ^ & *_'
# str_1 = "Hello!, he said, -- I have $45 & you?"
# no_punc = ""
# for char in str_1:
#               if char not in punc:
#                              no_punc = no_punc + clear
# print (no_punc)
# # NameError: name 'clear' is not defined.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def lines(numBreaks):
    for i in range(numBreaks):
        print("")

def spacing(blanks, dashes):
    lines(blanks)
    print("- " * dashes)
    lines(blanks)

lines(1)
print("TITLE")
lines(1)



import turtle               # imports the turtle module for use in this program

turtle.shape("turtle")      # changes the shape from a default arrow to a turtle

turlte.speed("8")           # fast speed on scale from 1-9 (0 and >=10 are fastest)

turtle.forward(50)



lines(2)
print("- - - - -")
lines(2)


# FutureCoder

# word = "Hello"
# name = "World"
# sentence = word + ' ' + name
# print(sentence)
# word = "Goodbye"
# print(sentence)

name = "Hello, World!"

# for character in name:
#     # print("---", end = "")
#     # print(character)
#     print(name)

# hello = "Hello"
# print(hello)        # should print: Hello
# hello = hello + '!' # should reassign hello variable to: Hello!
# print(hello)        # should print: Hello!

# line = ""

# for char in name:
#     # print(line)
#     line = char + line    # += char + " "
#     print(line)

def fancyLine(string):
    print("+", end = "")
    for char in string:
        print("-", end = "")
    print("+")

# fancyLine(name)
# print("|", end = "")
# print(name, end = "")
# print("|")
# fancyLine(name)

def fancierLine(string):
    print("+", end = "")
    for char in string:
        print(char, end = "")
    print("+")

# spaces = " " * len(name)
# spaces = " " * name[i]

# fancierLine(name)
# for char in name:
#     print(char, end = "")
#     print(spaces, end = "")
#     # for i in name:
#     #     print(" ", end = "")
#     print(char)
# fancierLine(name)

sp = ""

for char in name:
    print(sp + char)
    sp += " "


lines(2)
print("- - - - -")
lines(2)


# condition = True
# print(condition)

# condition = False
# print(condition)

# if True:
#     print("This gets printed")

# if False:
#     print("This does not")

sentence = "Hello World"
include = False
# excited = True
# confused = True

# if excited:
#     new_sentence = ""
#     for char in sentence:
#         new_sentence += char + "!"
#     sentence = new_sentence
#     sentence += "!"
# if confused:
#     sentence += "?"

new_sentence = ""

for char in sentence:
    if include:
        new_sentence += char
    include = True

print(new_sentence)


lines(2)
print("- - - - -")
lines(2)


# condition = False

# if condition:
#     print("Yes")
# else:
#     print("No")


# sentence = "Hello World"
# excited = False

# if excited:
#     char = "!"
# else:
#     char = "."

# sentence += char

# #     sentence = sentence.upper()
# # else:
# #     sentence = sentence.lower()

# print(sentence.title())

# print(sentence[0].upper())


# cap = True

# for char in sentence:
#     if cap:
#         print(char.upper(), end = "")
#         cap = False
#     else:
#         print(char.lower(), end = "")


sentence = "One more exercise, and then you can relax."
cap = True

# for char in sentence:
#     if sentence[char]%2:
#         print(char.upper(), end = "")
#     else:
#         print(char.lower(), end = "")

# print(sentence[1])

for char in sentence:
    if cap:
        print(char.upper(), end="")
        cap = False
    else:
        print(char.lower(), end="")
        cap = True

# print(1 + 2 == 3)
# print(4 + 5 == 6)
# print("ab" + "c" == "a" + "bc")



# name = "kesha"
# new_name = ""

# for c in name:
#     if c == "s":
#         c = "$"
#     if c == "e":
#         c = "3"
#     if c == "a":
#         c = "@"
#     new_name += c

# print(new_name)


lines(2)
print("- - - - -")
lines(2)


dna = "AGTAGCGTC"
opposite_dna = ""

for char in dna:
    if char == "A":
        char = "T"
    elif char == "T":
        char = "A"
    elif char == "G":
        char = "C"
    elif char == "C":
        char = "G"
    opposite_dna += char

print(opposite_dna)


spacing(2,5)

# sentence = 'The e key on my keyboard is broken'
# new_sentence = ''

# for c in sentence:
#     if c != 'e':
#         new_sentence += c

# print(new_sentence)


# percentage = 73

# if percentage < 40:
#     grade = "F"
# elif percentage < 60:
#     grade = "C"
# elif percentage < 80:
#     grade = "B"
# else:
#     grade = "A"

# print(grade)


x1 = "Alice"
x2 = "Bob"
x3 = "Charlie"

if x1 < x2 and x1 < x3:
    print(x1)
elif x2 < x1 and x2 < x3:
    print(x2)
elif x3 < x1 and x3 < x2:
    print(x3)


spacing(2,5)


words = ["This", "is", "a", "list"]

# for word in words:
#     print(word)



# x = 1
# things = ["Hello", x, x + 3]
# print(things)



# numbers = [3, 1, 4, 1, 5, 9]
# total = 0

# for number in numbers:
#     total += number
# print(total)



separator = " - "

totalW = ""

# for word in range(len(words) - 1):
for word in words:
    if word == words[len(words) - 1]:
        totalW += word
    else:
        totalW += word + separator
print(totalW)


spacing(1, 11)

# numbers = [1, 2] + [3, 4]
# print(numbers)

# new_numbers = []
# new_numbers += numbers
# new_numbers += [5]
# print(new_numbers)



numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
newNum = []

# for num in numbers:
#     num = num * 2
#     newNum += [num]

# # print(numbers)
# print(newNum)



for num in numbers:
    if num > 5:
        newNum.append(num)
print(newNum)


spacing(1,11)



things = ["This", "is", "a", "list"]

thing_to_find = "is"
# thing_to_find = "other"



# for thing in things:
#     if thing == thing_to_find:
#         print(True)
#         break
#     else:
#         print(False)

# def thing_in_things(thing_to_find, things):
#     if thing ==



# isThing = ""

# for thing in things:
#     if thing == thing_to_find:
#         isThing = True
#         break
#     else:
#         isThing = False
# print(isThing)



# found_thing = False

for thing in things:
    if thing == thing_to_find:
        found_thing = True
        break
    else:
        found_thing = False
print(found_thing)


spacing(1,11)


words = ["This", "is", "a", "list"]
# indices = [0, 1, 2, 3]
# indices = range(4)
# print(indices)
# print("")

# for index in indices:
#     print(indices[index])
    # print(index)
    # print(words[index])

# print(words[1])
# print(words[2])
# print(words[3])
# print(words[10])

# print(indices[0])
# print(indices[1])
# print(indices[2])
# print(indices[3])

# print(words[len(words) - 1])

# for index in range(len(words)):
#     print(index)
#     print(words[index])

print("EXERCISE 1: Print the numbers from 1 to 100 inclusive.")
for i in range(101):
    print(i, end = " ")

print("")
print("")
print("EXERCISE 2: Print your name 100 times.")
for i in range(100):
    print(i+1, "Dani", end = " * ")

print("")
print("")
print("EXERCISE 3: Print each word in a list words except for the last one.")
for word in range(len(words) - 1):
    print(words[word], end = " ")

print("")
print("Whole list:", end = " ")
for word in words:
    print(word, end=" ")

print("")
print("")
print("EXERCISE 4: Print each word in words in reverse order, i.e. print the last word, then the second last word, etc.")
for word in range(len(words) - 1, -1, -1):
    print(words[word], end = " ")


spacing(2, 7)

words = ["This", "is", "a", "list"]
# indices = [0, 1, 2, 3]
# indices = range(4)
# print(indices)
# print("")

# for index in indices:
#     print(indices[index])
    # print(index)
    # print(words[index])

# print(words[1])
# print(words[2])
# print(words[3])
# print(words[10])

# print(indices[0])
# print(indices[1])
# print(indices[2])
# print(indices[3])

# print(words[len(words) - 1])

# for index in range(len(words)):
#     print(index)
#     print(words[index])

print("EXERCISE 1: Print the numbers from 1 to 100 inclusive.")
for i in range(101):
    print(i, end = " ")

print("")
print("")
print("EXERCISE 2: Print your name 100 times.")
for i in range(100):
    print(i+1, "Dani", end = " * ")

print("")
print("")
print("EXERCISE 3: Print each word in a list words except for the last one.")
for word in range(len(words) - 1):
    print(words[word], end = " ")

print("")
print("Whole list:", end = " ")
for word in words:
    print(word, end=" ")

print("")
print("")
print("EXERCISE 4: Print each word in words in reverse order, i.e. print the last word, then the second last word, etc.")
for word in range(len(words) - 1, -1, -1):
    print(words[word], end = " ")

print("")
print("")
print("EXERCISE 5: Revisit the bonus problem at the end of the Introducing Lists page, whether or not you completed it. It's now much easier with range and len!")

separator = "- "
total = ""

for word in range(len(words) - 1):
    print(words[word], separator, end = "")
print(words[len(words) - 1])


spacing(3,33)

# things = ["on", "the", "way," "to", "the", "store"]
# to_find = "the"

# for i in range(len(things)):
#     if things[i] == to_find:
#         print(i)
#         break

string1 = "Goodbye"
string2 = "Elizabeth"

length1 = len(string1)
length2 = len(string2)

if length1 > length2:
    range_num = length1
else:
    range_num = length2

# Works only if len(string1) == len(string2)
for i in range(range_num):
    print(string1[i], string2[i])
    string1 += " "
    string2 += " "


spacing(2,22)


# print(len)
# print(print)
# print(callable(len))

# f = "a string"
# print(callable(f))
# f()

# things = [1, 2, 3]
# length = len(things)
# printed = print(length)
# print(printed)

# print(print(3))

# things = print([1, 2, 3])
# length = len(things)

word = "Hello"

# print(word.upper)
# print(word.upper())

# word.append("!")


spacing(5, 55)

# nums = [1, 2, 3]
# nums.append(55)
# print(nums)

# print(range(len(nums)))

# print(nums[3])

# nums += [777, 99999]
# print(nums)



# nums = [1, 2, 3]
# new_nums = nums + [4, 5]
# print(new_nums)
# print(nums)
# nums.append(4)
# print(nums)



# nums[2] = 333
# print(nums)



# nums = [1, 2, 3]
# nums[1] = 9
# print(nums)

# nums[7] = 7
# print(nums)



# myList = [1, 3, 5, 7, 9]
# onMyList = myList.index(5)          # (5) returns 2; if not on list, returns error
# print(onMyList)



# nums = [1, 2, 3]
# print(nums.pop(1))
# print(nums)

# print(nums.pop(1))
# print(nums)

# print(nums.pop(0))
# print(nums)



# nums = [1, 2, 3, 3, 2, 1]
# nums.remove(2)
# print(nums)

# print(callable(nums.remove(1)))

# nums = [1, 2, 3]
# nums.remove(1)
# print(nums)



# x = ["a", "b", "c"]
# # x.append(x.pop(0))        # ['b', 'c', 'a']
# # x[len(x) - 1] = x[0]      # ['a', 'b', 'a']
# # print(x)
# y = x + [x[0]]              # ['a', 'b', 'c', 'a']
#     # for some reason x.append(x[0]) only works with print(x), but returns "None" for print(y)
# print(y)



x = [1, 2, 0, 3]
x.pop(x.index(0))        # equivalent to x.remove(0)
print(x)


spacing(3, 33)


# print(sorted([2, 9, 1, 8, 5, 6]))



# nums = [2, 9, 1, 8, 5, 64]
# print(7 in nums)    # False
# print(2 in nums)    # True



# print(sum([5, 3, 4]))      # 12


#print([1, 2, 3, 2, 7, 2, 5].count(2))      # 3 (number of times "2" appears in the list)



# x = [1, 2, 0, 3]
# y = x.count(1) > 0        # equivalent to y = 1 in x (True)
# print(y)



# x = [15, 12, -6, 3]
# y = sum(x) / len(x)         # returns the average (mean) = 6.0
# print(y)




# x = 100
# y = sum(range(x + 1))       # adds up 1 + 2 + ... + 100 (inclusive) = 5050
# print(y)



x = [12, -6, 2, -1, 3]
y = sorted(x)[1]            # returns the second smallest value in x
print(y)


spacing(2, 111)



# string = "feed the dog and the cat"

# print("the" in string)

# print(string.count("the"))      # should be 2
# print(string.index("the"))      # not sure, maybe 5? -> YES!



# "Python".append(" is cool!")      # error, strings are immutable



sentence = "Python rocks!"
new_sentence = sentence.upper()
newer_sentence = sentence.lower()
print(sentence)
print(new_sentence)
print(newer_sentence)


# print(max([21, 55, 4, 91, 62, 49]))


# nums = [1, 2, 3, 4, 5]
# nums.insert(2, 9)             # https://www.w3schools.com/python/ref_list_insert.asp
# print(nums)


# print(dir([]))



list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list2 = list1.copy()
list2 = list1

print(list1)
print(list2)
print(list1 == list2)

print(list1 is list2)

list1.append(4)

print(list1)
print(list2)




numbers = [10, 7, 8, 3, 12, 15]
# big_numbers = numbers.copy()

# for number in numbers:
#     if number <= 10:
#         big_numbers.remove(number)
# # for i in range(len(numbers)):
# #     number = numbers[i]
# #     if number <= 10:
# #         numbers.pop(i)
# print(big_numbers)


big_numbers = []
for number in numbers:
    if number > 10:
        big_numbers.append(number)
print(big_numbers)


spacing(1,151)


# name = 'Alice'

# print('Alice's Diner')
# print("Alice's Diner")

# print('Alice' == "Alice")   # True
# print('alice' == 'Alice')   # False

# print("Special cases aren't special enough to break the rules.")

# print('"Talk is cheap. Show me the code." - Linus Torvalds')

# friend = "Bob"
# meal = 'lunch'

# print(name + " went to " + meal + " with " + friend + ".")
# print(f"{name} went to {meal} with {friend}.")        # Equivalent output

# age = 20

# print("Hello " + name + ". You are " + age + " years old.")     # Yields error b/c int's can't be concatenated with strings
# print(f"Hello {name}. You are {age} years old.")      # Achieves the desired result

people = ["Alice", "Bob", "Charlie"]

# print('There are' + people.length() + 'people waiting, the first one's name is' + people.1 + '.')

# print(people.length())  # Invalid
# print(people.1)         # Invalid

print(f"There are {len(people)} people waiting, the first one's name is {people[0]}.")



spacing(2, 99)

# INTRODUCING NESTED LOOPS

# for letter in "ABC":
#     print(letter)
#     for number in range(4):
#         print(f"{letter} {number}")
#     print("---")

# Nested loop to print multiplication tables 1-12 with --- in between
# for first_num in range(1, 13):
#     for second_num in range(1,13):
#         print(f"{first_num} x {second_num} = {first_num * second_num}")
#     print("---")

# Print all tournaments for list [players] where no one plays themself, but each plays the others twice
# players = ["Alice", "Bob", "Charlie"]
# for first_player in players:
#     for second_player in players:
#         if first_player != second_player:
#             print(f"{first_player} vs {second_player}")

# Print all possible 4-letter passwords using letters [A, B, C, D]
# letters = "ABCD"
# for first_letter in letters:
#     for second_letter in letters:
#         for third_letter in letters:
#             for fourth_letter in letters:
#                 print(f"{first_letter}{second_letter}{third_letter}{fourth_letter}")

# Print upside-down triangle of +s with sides of length size
# size = 5
# for i in range(size, 0, -1):
#     # print("+" * i)        # Correct but can't use "*" for this exercise
#     # for j in range(size, 0, -1):
#     #     print("+" * j)
#     for j in range(i):
#         print("+", end = "")
#     print("")

# # Print all tournaments for list [players] where no one plays themself or another more than once
# players = ["Charlie", "Alice", "Dylan", "Bob"]
# other_players = players.copy()
# for first_player in players:
#     other_players.remove(first_player)
#     # print(other_players)
#     for second_player in other_players:
#         # for third_player in players:
#         #     for fourth_player in players:
#         # if first_player != second_player:
#         print(f"{first_player} vs {second_player}")

# print("-----")

players = ['Charlie', 'Alice', 'Dylan', 'Bob']
for i in range(len(players)):
    for j in range(len(players)):
        if i < j:
            print(f'{players[i]} vs {players[j]}')

# other_players = other_players.pop(0)
# print(other_players)

# fruits = ['apple', 'banana', 'cherry']
# # x = fruits.pop(1)
# # print(x)
# fruits.remove(fruits[-1])
# # print(y)
# print(fruits)


spacing(1, 11)


# a = 2
# b = 3
# c = 4
# d = 5
# print(a * b + c * d)



word = 'Amazing'
vowels = []
consonants = []
for letter in word:
    if letter.lower() in 'aeiou':
        vowels.append(letter)
    else:
        consonants.append(letter)
print(vowels)
print(consonants)



# strings = ["abc", "def", "ghi"]



# Printing the first character of the second entry on the [list]

# second_string = strings[1]
# print(second_string)      # def

# first_letter = second_string[0]
# print(first_letter)       # d

# print(strings[1][0])      # d



# Printing the last letter of the second-to-last string

# print(strings[-2][-1])    # f



# Nested subscripting on lists of lists
strings = [["hello", "there"], ["how", "are", "you"]]

# print(strings[1][0])      # prints "how," the first element of the second sub-list

# Printing the first letter of the third string in the second sublist
# print(strings[1][2][0])     # y

# Not sure why but this doesn't work:
# new = strings.copy()
# new = new[1].append("today?")
# print(new[1])

strings[1].append("today?")
print(strings)                # works: [['hello', 'there'], ['how', 'are', 'you', 'today?']]


numbers = [[1, 2, 3], [4, 5], [6], []]

for sublist in numbers:
    for num in sublist:
        print(num)
    print("---")

spacing(1,33)

# strings = [
#     [
#         "hello there",
#         "how are you",
#     ],
#     [
#         "goodbye world",
#         "hello world",
#     ]
# ]

# word = "world"


# # Print all lines that contain a word

# for substring in strings:
#     for i in substring:
#         if word in i:
#             print(i)


# Print whether or not the sublists contain a word

# for substring in strings:
#     for words in substring:
#         for i in words:
#             if word in substring:
#             # if substring[i:len(word)] == word:
#                 print("True")
#             else:
#                 print("False")

# onList = False

# for sublist in strings:
#     for element in sublist:
#         if word in element:
#         #     print(True)
#         # else:
#         #     print(False)
#             onList = True
#     if onList == True:
#         print(True)
#     else:
#         print(False)


# Print whether or not the full list contain a word

# word = "Python"     # False
# word = "hello"      # True

# onList = False

# for sublist in strings:
#     for element in sublist:
#         if word in element:
#         #     print(True)
#         # else:
#         #     print(False)
#             onList = True
# if onList == True:
#     print(True)
# else:
#     print(False)


# strings = ["abc", "def", "ghi"]

# for element in strings:
#     for i in element:
#         print(i)

# print(strings[0][1])

# wordIndex = 0
# letterIndex = 0

# for word in strings:          # range(len(strings)):    # for "word" between [0, 3)
#     for letter in word:
#         wordIndex = strings.index(word)
#         letterIndex = strings.index(letter)
#         print(strings[wordIndex][letterIndex])

# print(strings[0][0], strings[1][0], strings[2][0])  # a d g with spaces

# print(strings[0][0], end = "")
# print(strings[1][0], end = "")
# print(strings[2][0])                # adg no spaces

# print(strings[0][1], end = "")
# print(strings[1][1], end = "")
# print(strings[2][1])

# print(strings[0][2], end = "")
# print(strings[1][2], end = "")
# print(strings[2][2])


# for word in
# for letter in range(len(word)):
# print(word)


strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]

# longest = 0
# for i in strings:
#     if len(i) > longest:
#         longest = len(i)            # Works
#     # else:
#     #     strings[i].append(" ")
# print(longest)

# for i in strings:
#     if len(i) < longest:
#         strings[i].append("*")      # Doesn't work unless same len
# print(strings)

# for word in strings:
#     wordElement = strings.index(word)
#     for letter in word:
#         letterElement = word.index(letter)
#         # if letterElement <= wordElement:
#         print(strings[wordElement][letterElement], end = "")
#         # else:
#         #     print(strings[letterElement][wordElement - 1], end = "")
#     print("")

# print(strings.index("abc"))       # abc = 0, but a = Error b/c it's not its own element/word


# print(strings[0][0], end = "")
# print(strings[1][0], end = "")
# print(strings[2][0], end = "")
# print(strings[3][0], end = "")
# print(strings[4][0], end = "")
# print(strings[5][0])

# print(strings[0][1], end = "")
# print(strings[1][1], end = "")
# print(strings[2][1], end = "")
# print(strings[3][1], end = "")
# print(strings[4][1], end = "")
# print(strings[5][1])

# print(strings[0][2], end = "")
# print(strings[1][2], end = "")
# print(strings[2][2], end = "")
# print(strings[3][2], end = "")
# print(strings[4][2], end = "")
# print(strings[5][2])

for word in strings:
    wordElement = strings.index(word)
    for letter in word:
        letterElement = word.index(letter)
        # if letterElement <= wordElement:
        print(strings[wordElement][letterElement], end="")
        # else:
        #     print(strings[letterElement][wordElement - 1], end = "")
    print("")
    print("")

    print("t-r-y-i-n-g---a-g-a-i-n")

    # strings = ["abc", "def", "ghi"]

    # for element in strings:
    #     for i in element:
    #         print(i)

    # print(strings[0][1])

    # wordIndex = 0
    # letterIndex = 0

    # for word in strings:          # range(len(strings)):    # for "word" between [0, 3)
    #     for letter in word:
    #         wordIndex = strings.index(word)
    #         letterIndex = strings.index(letter)
    #         print(strings[wordIndex][letterIndex])

    # print(strings[0][0], strings[1][0], strings[2][0])  # a d g with spaces

    # print(strings[0][0], end = "")
    # print(strings[1][0], end = "")
    # print(strings[2][0])                # adg no spaces

    # print(strings[0][1], end = "")
    # print(strings[1][1], end = "")
    # print(strings[2][1])

    # print(strings[0][2], end = "")
    # print(strings[1][2], end = "")
    # print(strings[2][2])

    # for word in
    # for letter in range(len(word)):
    # print(word)

    strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]
    # strings = ["abc", "def", "ghi"]

    longest = 0
    for i in strings:
        if len(i) > longest:
            longest = len(i)  # Works
    #     # else:
    #     #     strings[i].append(" ")
    # print(longest)

    for i in range(longest):
        for j in range(len(strings)):
            print(strings[j][i], end="")
        print("")

    # for i in strings:
    #     if len(i) < longest:
    #         strings[i].append("*")      # Doesn't work unless same len
    # print(strings)

    # for word in strings:
    #     wordElement = strings.index(word)
    #     for letter in word:
    #         letterElement = word.index(letter)
    #         # if letterElement <= wordElement:
    #         print(strings[wordElement][letterElement], end = "")
    #         # else:
    #         #     print(strings[letterElement][wordElement - 1], end = "")
    #     print("")

    # print(strings.index("abc"))       # abc = 0, but a = Error b/c it's not its own element/word

    # print(strings[0][0], end = "")
    # print(strings[1][0], end = "")
    # print(strings[2][0], end = "")
    # print(strings[3][0], end = "")
    # print(strings[4][0], end = "")
    # print(strings[5][0])

    # print(strings[0][1], end = "")
    # print(strings[1][1], end = "")
    # print(strings[2][1], end = "")
    # print(strings[3][1], end = "")
    # print(strings[4][1], end = "")
    # print(strings[5][1])

    # print(strings[0][2], end = "")
    # print(strings[1][2], end = "")
    # print(strings[2][2], end = "")
    # print(strings[3][2], end = "")
    # print(strings[4][2], end = "")
    # print(strings[5][2])

    # strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]

    # for word in strings:
    #     wordElement = strings.index(word)
    #     for letter in range(len(word) + 1):
    #         # print(wordElement, letter)
    #         print(strings[letter][wordElement], end = "")
    #     print("")


    spacing(2, 44)

    # strings = ["abc", "def", "ghi"]

    # for element in strings:
    #     for i in element:
    #         print(i)

    # print(strings[0][1])

    # wordIndex = 0
    # letterIndex = 0

    # for word in strings:          # range(len(strings)):    # for "word" between [0, 3)
    #     for letter in word:
    #         wordIndex = strings.index(word)
    #         letterIndex = strings.index(letter)
    #         print(strings[wordIndex][letterIndex])

    # print(strings[0][0], strings[1][0], strings[2][0])  # a d g with spaces

    # print(strings[0][0], end = "")
    # print(strings[1][0], end = "")
    # print(strings[2][0])                # adg no spaces

    # print(strings[0][1], end = "")
    # print(strings[1][1], end = "")
    # print(strings[2][1])

    # print(strings[0][2], end = "")
    # print(strings[1][2], end = "")
    # print(strings[2][2])

    # for word in
    # for letter in range(len(word)):
    # print(word)

    # strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]
    # strings = ["abc", "def", "ghi"]
    # strings = ["abcqwe", "def", "ghiq"]

    # longest = 0
    # for i in strings:
    #     if len(i) > longest:
    #         longest = len(i)            # Works
    #     # else:
    #     #     strings[i].append(" ")
    # print(longest)

    # for i in range(longest):
    #     if len(strings[i]) >= longest:
    #         for j in range(len(strings)):
    #             if len(strings[j]) <= longest: # < len(strings):
    #                 print(strings[j][i], end = "")
    #     else:
    #         print(" ")
    # print("")

    # for i in strings:
    #     if len(i) < longest:
    #         strings[i].append("*")      # Doesn't work unless same len
    # print(strings)

    # for word in strings:
    #     wordElement = strings.index(word)
    #     for letter in word:
    #         letterElement = word.index(letter)
    #         # if letterElement <= wordElement:
    #         print(strings[wordElement][letterElement], end = "")
    #         # else:
    #         #     print(strings[letterElement][wordElement - 1], end = "")
    #     print("")

    # print(strings.index("abc"))       # abc = 0, but a = Error b/c it's not its own element/word

    # print(strings[0][0], end = "")
    # print(strings[1][0], end = "")
    # print(strings[2][0], end = "")
    # print(strings[3][0], end = "")
    # print(strings[4][0], end = "")
    # print(strings[5][0])

    # print(strings[0][1], end = "")
    # print(strings[1][1], end = "")
    # print(strings[2][1], end = "")
    # print(strings[3][1], end = "")
    # print(strings[4][1], end = "")
    # print(strings[5][1])

    # print(strings[0][2], end = "")
    # print(strings[1][2], end = "")
    # print(strings[2][2], end = "")
    # print(strings[3][2], end = "")
    # print(strings[4][2], end = "")
    # print(strings[5][2])

    # strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]

    # for word in strings:
    #     wordElement = strings.index(word)
    #     for letter in range(len(word) + 1):
    #         # print(wordElement, letter)
    #         print(strings[letter][wordElement], end = "")
    #     print("")

    # print(strings[0][0], end = "")
    # print(strings[1][0], end = "")
    # print(strings[2][0])                # adg no spaces

    # print(strings[0][1], end = "")
    # print(strings[1][1], end = "")
    # print(strings[2][1])

    # print(strings[0][2], end = "")
    # print(strings[1][2], end = "")
    # print(strings[2][2])

    # print(strings[0][3], end = "")
    # print(strings[1][3], end = "")
    # print(strings[2][3] in strings)

    # for words in range(longest):
    #     for letters in range(len(strings)):
    #         if strings[j][i] in strings:
    #             print(strings[j][i], end = "")
    #         else:
    #             print(" ", end = "")
    #     print("")

    # print(range(longest))
    # print(range(len(strings)))
    # print(longest)
    # print(len(strings))

    # for word in range(longest):
    #     wordElement = strings.index(word)
    #     print(wordElement)
    #     for letter in range(len(strings)):
    #         letterElement = word.index(letter)
    #         print(letterElement)

    # for word in strings:
    #     wordElement = strings.index(word)
    #     for letter in range(len(word) + 1):
    #         # print(wordElement, letter)
    #         print(strings[letter][wordElement], end = "")
    #     print("")

    # strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]
    strings = ["abcqwe", "def", "ghiq"]

    # strings = ["abc", "def", "ghi"]

    # longest = 0
    # for i in strings:
    #     if len(i) > longest:
    #         longest = len(i)

    # for i in range(longest):
    #     # iIndex = len(strings[i])
    #     for j in range(len(strings)):
    #         # if strings[j][i] in strings[j]:
    #         # if len(strings[i]) <= len(strings[j]):
    #         # jIndex = len(strings[i][j])
    #         # if j > iIndex:
    #         if len(strings[i]) >= longest:
    #         # print(iIndex)
    #         # if iIndex > longest:
    #             print(strings[j][i], end="")
    #         else:
    #             strings[i] += " "
    #             # print(" ", end = "")
    #     print("")

    wordLengths = []

    for word in strings:
        wordLengths.append(len(word))
    # print(wordLengths)
    maxLength = max(wordLengths)
    # print(maxLength)

    for i in range(maxLength):
        printout = ""
        for word in strings:
            if i < len(word):
                printout += word[i]
            else:
                printout += " "
        print(printout)


spacing(1, 55)


# def say_hello(person_name):
#     print(f"Hello {person_name}!")
#     print("How are you?")

# say_hello("Alice")
# say_hello("Bob")


# def print_twice(x):
#     print(x)
#     print(x)

# print_twice("Hello")


# def print_many(thing_to_print, times_to_print):
#     for i in range(times_to_print):
#         print(thing_to_print)

# print_many("Danimo", 4)


# def print_many(thing, n):
#     for _ in range(n):
#         print(thing)

# print_many("Hello", 3)


def print_many(n, thing):
    for _ in range(n):
        print(thing)


# print_many(3, "Hello")

def print_twice(x):
    print_many(2, x)


print_twice("Hello")


spacing(1, 11)


def double(x):
    return (x * 2)


# number = 5
# twice = double(number)
# print(number)
# print(twice)
# print("")

# double(number)
# print(number)
# print("")

def quadruple(x):
    return (double(double(x)))


# print(quadruple(2))
# print("")
# print(quadruple(7))


# print(f"{'abc'} {repr('abc')}")         # abc 'abc'

def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")


# assert_equal(double(2), 4)
# # assert_equal(double(2), 5)
# assert_equal(double(5), 10)
# # assert_equal(quadruple(5), 20)

# assert_equal(quadruple(2), 8)
# assert_equal(quadruple(5), 20)


def surround(string, sides):
    return f"{sides}{string}{sides}"  # assert_equal doesn't work with print()  b/c no value returned
    # return sides + string + sides         # also works


# surround("more", "++")
# assert_equal(surround("more", "++"), "++more++")

# surround("the same", "=")
# assert_equal(surround("the same", "="), "=the same=")


def alert(string, level):
    new_string = surround(string, " ")
    # new_sides = "!" * level
    # new_level = surround(new_string, "!" * level)
    # return surround(new_string, new_level)
    # return new_level
    # return surround(f" {string} ", level * "!")

    for i in range(level):
        new_string = surround(new_string, "!")

    return new_string


# alert("Warning", 2)
# alert("DANGER", 4)

# f"{name} went to {meal} with {friend}."

string = 'Warning'
level = 2

print(alert(string, level))

print("- - - CLEAN   VERSION  - - -")


def surround(string, sides):
    return f"{sides}{string}{sides}"  # assert_equal doesn't work with print()  b/c no value returned


def alert(string, level):
    new_string = surround(string, " ")

    for i in range(level):
        new_string = surround(new_string, "!")

    return print(new_string)


alert("Warning", 2)
alert("DANGER", 4)

string = 'Warning'
level = 2

alert(string, level)

spacing(3,55)


# def foo():
#     return 1
#     return 2

# print(foo())          # 1 b/c only the first "return" run will be executed



# def double_numbers(numbers):
#     for x in numbers:
#         return x * 2

# assert_equal(double_numbers([1, 2, 3]), [2, 4, 6])
# # Fail b/c will return 2, not a list



# def double_numbers(numbers):
#     doubles = []
#     for x in numbers:
#         doubles.append(x * 2)
#     return doubles

# assert_equal(double_numbers([1, 2, 3]), [2, 4, 6])      # OK
# assert_equal(double_numbers([1, 2, 3]), [2, 4, 7])      # Error! [2, 4, 6] != [2, 4, 7]



def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == "b":
                # return letter         # a 0 // a 1 // a 2 // b 0 (END)
                break                   # a 0 // a 1 // a 2 // b 0 // c 0 // c 1 // c 2

foo()

spacing(2, 222)

print("Introducing 'or'")

# def is_friend(name):
#     return name in ["Alice", "Bob"]
#     # return name == "Alice" or "Bob"
#     # return name == "Alice" or name == "Bob"
#     #     return True
#     # else:
#     #     return False

# assert_equal(is_friend("Alice"), True)
# assert_equal(is_friend("Bob"), True)
# assert_equal(is_friend("Charlie"), False)

# print("Alice" in ["Alice", "Bob"])
# print("Charlie" in ["Alice", "Bob"])



def is_valid_percentage(x):
    if x < 0 or x > 100:
        return False
    else:
        return True
    # return x >= 0 and x <= 100        # Can't use "and" here
    # if x >= 0 and x <= 100:           # Equivalent written out
    #     return True
    # else:
    #     return False

assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)

spacing(1,33)

print("Introducing 'and'")

def is_valid_percentage(x):
    return 0 <= x <= 100
    # return x >= 0 and x <= 100
    # return 0 <= x and x <= 100        # Equivalent with more math-y notation

# assert_equal(is_valid_percentage(-1), False)
# assert_equal(is_valid_percentage(0), True)
# assert_equal(is_valid_percentage(50), True)
# assert_equal(is_valid_percentage(100), True)
# assert_equal(is_valid_percentage(101), False)



def all_equal(row):
    return row[0] == row[1] == row[2]

assert_equal(all_equal(["X", "X", "X"]), True)
assert_equal(all_equal(["O", "O", "O"]), True)
assert_equal(all_equal(["X", "O", "X"]), False)



spacing(2,111)

print("Multi-Line Statements")

# is_friend = name == "Alice" or            # Invalid syntax b/c "or" considered incomplete
#             name == "Bob"

name = "Bob"

is_friend1 = name == "Alice" or \
             name == "Bob"
print(is_friend1)     # True for "Bob"

is_friend2 = (name == "Alice" or
              name == "Bob")
print(is_friend2)     # True for "Bob"

is_friend3 = [name == "Alice",
              name == "Bob"]
print(is_friend3)      # With "or" = [True] for "Bob" -- list
                       # With "," = [False, True] for "Bob" -- list

print(name == "Alice" or
      name == "Bob")    # True for "Bob"

spacing(2,55)

print("Combining 'and' & 'or'")

# My function:
def diagonal_winner(board):
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    return (row1[0] == row2[1] == row3[2] or
            row1[2] == row2[1] == row3[0])


# Another working function:
def diagonal_winner(board):
    middle = board[1][1]
    return (
            (middle == board[0][0] and
             middle == board[2][2]) or
            (middle == board[0][2] and
             middle == board[2][0])
    )

# Yet another working function:
def all_equal(row):
    return row[0] == row[1] == row[2]

def diagonal_winner(board):
    diagonal1 = all_equal([board[0][0],
                board[1][1], board[2][2]])
    diagonal2 = all_equal([board[2][0],
                board[1][1], board[0][2]])
    return diagonal1 or diagonal2

# Testing variables
# board =         [
#             ['X', 'O', 'X'],
#             ['X', 'X', 'O'],
#             ['O', 'O', 'X']
#         ]

# row1 = board[0]
# print(row1)         # ['X', 'O', 'X']


assert_equal(
    diagonal_winner(
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    False
)

spacing(3,111)

print("Introducing 'not'")


# b = True
# print(not b or b)       # True, equivalent to "(not b) or (b)"

def invalid_image(filename):
    # return not(filename.endswith(".jpg" or ".png"))     # Doesn't work for .png
    return not (filename.endswith(".jpg") or
                filename.endswith(".png"))


assert_equal(invalid_image("cat.jpg"), False)
assert_equal(invalid_image("dog.png"), False)
assert_equal(invalid_image("invoice.pdf"), True)


spacing(3,222)

print("Tic Tac Toe!!!")


'''