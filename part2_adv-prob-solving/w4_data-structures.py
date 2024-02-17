# 2024 Danielle K. Fluster
# Joy of Coding Academy
# Part 2 - Advanced Problem Solving

import danimo

# danimo.spacing(1, ".", 33)
# Renamed (with REFACTOR) "spacing" to "spaces" and "spacing2" to "spacing"
    # in danimo.py and auto-updated here!!!
# However, does NOT work for commented-out code, hard-coded strings, etc!!!
    # Tho appears to once they've been un-commented!?! :D

# # # Not working
# from Stack import *
# import Stack

def print_project_header(project, project_number, project_title):
    to_print = (f"{project.upper()} #{project_number}: {project_title}")
    danimo.spacing(2, "=", len(to_print))
    print(to_print)
    danimo.spacing(1, ".", len(to_print)//2)





# Week 4 - Data Structures & Algorithms
# Day 1 - What are Data Structures?

# HACKER RANK PROBLEMS
project = "HackerRank"


# HackerRank 01
# SUCCESS! @ 2024-02-15 ~6:30am
    # URL: https://www.hackerrank.com/challenges/arrays-ds/problem
    # Arrays - DS
    # EasyProblem Solving (Basic)
    # Max Score: 10
    # Success Rate: 93.25%
    # Accessing and using arrays.

project_number = 1
    # When set to "01", results in SyntaxError:
    # leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
project_title = "DS Arrays"

print_project_header(project, project_number, project_title)

def reverseArray(a):
    # Write your code here
    # a_reversed = []
    a_reversed = a.copy()
    # print(a_reversed)
    for i in range(len(a)):
        a_reversed[-1 - i] = a[i]
        # Equivalent to:
            # a_reversed[i] = a[-1 - i]
        # a_reversed.append(a[i])
            # Doesn't work; for [1, 2, 3] returns [1, 2, 3, 1, 2, 3]
    return a_reversed

def main1():
    a_test1 = [1, 2, 3]
    print(reverseArray(a_test1))

main1()       # All pass


# HackerRank 02
# SUCCESS! @ 2024-02-15 ~8am
# URL: https://www.hackerrank.com/challenges/2d-array/problem

project_number = 2
project_title = "2D DS Arrays"

print_project_header(project, project_number, project_title)

# All arrays will be 6 x 6

sampleArray1 = [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]

# print(sampleArray1)

sampleArray2 = [[-9, -9, -9, 1, 1, 1],
                [0, -9, 0, 4, 3, 2],
                [-9, -9, -9, 1, 2, 3],
                [0, 0, 8, 6, 6, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 1, 2, 4, 0]]

# print(sampleArray2)

sampleArray2_hourglasses = [[-63, -34, -9, 12],
                            [-10,   0, 28, 23],
                            [-27, -11, -2, 10],
                            [  9,  17, 25, 18]]

sampleArray3 = [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]]

# print(sampleArray2_hourglasses)

# print(max(max(sampleArray2_hourglasses)))
# Doesn't work b/c first prints out the max list (the last one based on the 0th number),
# then takes the max of that list -- i.e., returning 25 (not 28)

def arrayHourglasses(array):
    hourglasses = []
    for row in range(len(array) - 2):
        for col in range(len(array) - 2):
            hg1 = array[row][col]
            # print(hg1)
            hg2 = array[row][col+1]
            hg3 = array[row][col+2]
            hg4 = array[row+1][col+1]
            hg5 = array[row+2][col]
            hg6 = array[row+2][col+1]
            hg7 = array[row+2][col+2]
            hgTot = hg1 + hg2 + hg3 + hg4 + hg5 + hg6 + hg7
            hourglasses.append(hgTot)
            # print(hg)
            # print(array[i][j])
            # print(len(array) - 2)
    return max(hourglasses)

# print(arrayHourglasses(sampleArray2))

def arrayMax(array):
    max = 0
    for row in range(len(array)):
        # rowElement =
        for col in range(len(array)):
            # print(array[row][col])
            # colElement =
            if array[row][col] > max:
                max = array[row][col]
    # print(max)
    return max

# print(arrayMax(sampleArray2_hourglasses))       # 28 as expected!

def main_2():
    # for i in range(3):
    #     tester =
    print(arrayHourglasses(sampleArray1))
    print(arrayHourglasses(sampleArray2))
    print(arrayHourglasses(sampleArray3))

main_2()        # All pass





# Week 5 - Stacks & Queues
# Day 3 - Pseudocode & Templates

# JOY OF CODING ACADEMY PROJECT PROBLEMS
project = "JOC Academy"

# JOC Project 02 Prep
# Pseudocode: flip(stack)
    # Works on lists!

project_number = "2A"
project_title = "flip(stack)"

print_project_header(project, project_number, project_title)

print("See DS Arrays above!")



# Pseudocode: contue_uniq(queue)
    # Works on lists!

project_number = "2B"
project_title = "countue_uniq(queue)"

print_project_header(project, project_number, project_title)

# Testing functionality with lists

queue_test1 = [1, 1, 1, 2, 2, 4, 4, 4, 6]
queue_test2 = [3, 0, 4, 4, 4, 7, 7, 5, 5, 5]
queue_test3 = []

def count_uniq(queue):
    numbers = []
    unique = 0
    for i in range(len(queue)):
        if queue[i] not in numbers:
            numbers.append(queue[i])
            unique += 1
    # print(numbers)
    # print(unique)
    return unique

def main3():
    print(count_uniq(queue_test1), count_uniq(queue_test1) == 4)
        # print(numbers) = [1, 2, 4, 6]
        # print(unique) = 4
    # print("")
    print(count_uniq(queue_test2), count_uniq(queue_test1) == 5)
        # [3, 0, 4, 7, 5]
        # 5
    # print("")
    print(count_uniq(queue_test3), count_uniq(queue_test1) == 0)
        # []
        # 0
    print(count_uniq([1, 2, 1, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]))
        # 5

# main3()

print("Successful on main3()!")



# Pseudocode: postfix_to_infix(queue)
    # Works on lists!

project_number = "2C"
project_title = "postfix_to_infix(queue)"

print_project_header(project, project_number, project_title)

# Testing functionality with lists

# # # Not working and not updating GUI of "import" lines to indicate use
# stackTest.stack([1, 2, 3, 4, 5])
# stackTest.peek()
# print(stackTest)

regularList = [4, 5, "+", 7, 2, "-", "*"]
# print(regularList)
    # regularList2 = [4, 5, +, 7, 2, -, *] fails to print with
    # SyntaxError: invalid syntax for "+," (first instance)

# # Works as expected
# for i in range(len(regularList)):
#     if type(regularList[i]) == int:
#         print(regularList[i])

# print(type(1) == int)
# print(type("hello") == int)

# # Works as expected!
# tempStack = []      # Initialize a "stack" (list) for interim use
# desOutcome = ""     # Initialize an empty string for the outcome aggregator
# for i in range(len(regularList)):
#     if type(regularList[i]) == int:
#         # print(regularList[i])
#         tempStack.append(regularList[i])
#         print(tempStack)
#     else:
#         # print("Not an Int")
#         left = tempStack.pop(-2)
#         right = tempStack.pop(-1)
#         tempStack.append(f"({left} {regularList[i]} {right})")
#         # print(f"({left} {regularList[i]} {right})")
# desOutcome = "".join(tempStack)
# print(tempStack)
# print(desOutcome)

# testList = [1, 2, 3]
# testList.pop()      # Removes the last element with no argument,
#                         # or the element at the indexed value of a given argument
# print(testList)     # pop() returns [1, 2] (removes last element)
#                         # pop(-2) returns [1, 3] (removes -2nd element)

# testList = [1, 2, 3, 4, 5]
# testNum = str(testList.pop())
# print(testNum)
# print(testNum + 3)


def postfix_2_infix(queue):
    tempStack = []  # Initialize a "stack" (list) for interim use
    strOutcome = ""  # Initialize an empty string for the outcome aggregator
    for i in range(len(queue)):
        if type(queue[i]) == int:
            tempStack.append(queue[i])      # enq
        else:
            left = tempStack.pop(-2)        # deq
            right = tempStack.pop(-1)       # but in a different order
            tempStack.append(f"({left} {queue[i]} {right})")
    strOutcome = "".join(tempStack)
    return strOutcome

def main4():
    p2i_test1 = [1, 2, "+"]
    p2i_exRes1 = "(1 + 2)"
    print(postfix_2_infix(p2i_test1))
    print(postfix_2_infix(p2i_test1) == p2i_exRes1)
    print("")

    p2i_test2 = [5, 4, "*", 7, "+"]
    p2i_exRes2 = "((5 * 4) + 7)"
    print(postfix_2_infix(p2i_test2))
    print(postfix_2_infix(p2i_test2) == p2i_exRes2)
    print("")

    p2i_test3 = [2, 3, "*", 8, 5, "*", "+"]
    p2i_exRes3 = "((2 * 3) + (8 * 5))"
    print(postfix_2_infix(p2i_test3))
    print(postfix_2_infix(p2i_test3) == p2i_exRes3)

# main4()

print("Successful on main4()!")


# Pseudocode: Brace Matcher
    # I/P

project_number = "2D"
project_title = "Brace Matcher"

print_project_header(project, project_number, project_title)

# # Works as expected!
# testStr1 = "[()]"
# print(testStr1[0])

# # Note to self: use print with multiple arguments to achieve
    # some of what was asked for earlier in the class!
# def notMatcher(string):
#     for char in string:
#         print(char, "yay ")
# notMatcher("hello there you")

# strTest = "Hello, How Are You Today?"
# strOptions = ["h", "H"]
# # chk_strTest = (strTest[0] == ("h" or "H"))
#     # Doesn't work as expected; is False
# chk_strTest = strTest[0] in strOptions
#     # THIS ONE WORKS!
# print(chk_strTest)

# heythere = list("Hello My Darling, Hello My Baby")
# heythere.pop(0)
# print(heythere)

# def matcher(string):
#     # braces = ["(", ")", "[", "]", "{", "}"]
#         # Standard  braces[0] matches braces[1]
#         # Square    braces[2] matches braces[3]
#         # Curly     braces[4] matches braces[5]
#     braces = ["(", "[", "{", ")", "]", "}"]
#     braces_lefts = braces[:3]
#     # print(braces_lefts)
#     braces_rights = braces[3:]
#     # print(braces_rights)
#     matchStack = []
#     for i in range(len(string)):
#         if string[i] in braces:             # Stripping only braces
#             matchStack.append(string[i])
#     for j in range(len(matchStack)):
#         if matchStack[j] in braces_rights:
#             # print(matchStack[j])
#     # print(matchStack)
#     if matchStack == []:
#         return True
#     else:
#         return False

'''
def brace_matcher(string):
   brace_set    = [ "(", "[", "{", ")", "]", ")" ]
   brace_opens  = brace_set[:3]     # brace_opens  = [ "(", "[", "{" ]
   brace_closes = brace_set[3:]     # brace_closes = [ ")", "]", ")" ]
   tempStack = S[]
   unmatched = []

   for char in string:
      # if char in brace_set:     # Pushes all braces into tempStack
      #   tempStack.push(char)

      if char in brace_opens:     # Pushes only open braces to tempStack
         tempStack.push(char)

      elif char in brace_closes:
         next_brace = tempStack.peek()
         if    (char == brace_opens[0]) and (next_brace == brace_closes[0])
          orif (char == brace_opens[1]) and (next_brace == brace_closes[1])
          orif (char == brace_opens[2]) and (next_brace == brace_closes[2]):
            tempStack.pop()       # Pops topmost brace if matching
         else:
            return False
            # unmatched.append(char)            

   if tempStack = S[] and unmached = []:
      return True
   else:
      return False


def matcher(string):
    brace_set= ["(", "[", "{", ")", "]", "}"]
    braces_openers = braces[:3]
    braces_closers = braces[3:]
    braces = []
    matchStack = []

    # Stripping all characters except braces
    for i in range(len(string)):
        if string[i] in braces:
            braces.append(string[i])

    # Looping through and pushing given openers,
    # while checking & popping given closers
    for j in range(len(braces)):
        if braces[j] in braces_openers:
            matchStack.insert(0, braces[j])
        elif braces[j] in braces_closers:
            # if matchStack.peek() !=

            # print(matchStack[j])
    # print(matchStack)
    if matchStack == []:
        return True
    else:
        return False
        
    # braces_in_str = []
    # for char in str:
    #     if char in braces_all:
    #         braces_in_str.append(char)
    # print(braces_in_str)
'''

def main5():
    match_test1 = "[()]"
    match_expRes1 = True
    match_test2 = "[("
    match_expRes2 = False
    match_test3 = "something else"
    match_expRes3 = True

    matcher(match_test1)        # Used to test with printed function outcome
    # print(matcher(match_test1))
    # print(matcher(match_test1) == match_expRes1)
    print("")

    matcher(match_test2)
    # print(matcher(match_test2))
    # print(matcher(match_test2) == match_expRes2)
    print("")

    matcher(match_test3)
    # print(matcher(match_test3))
    # print(matcher(match_test3) == match_expRes3)
    print("")

# main5()
