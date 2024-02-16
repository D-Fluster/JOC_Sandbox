import danimo

# Part 2 - Advanced Problem Solving
# Week 4 - Data Structures & Algorithms
# Day 1 - What are Data Structures?

project = "HackerRank"

def print_project_header(project, project_number, project_title):
    to_print = (f"{project.upper()} #{project_number}: {project_title}")
    danimo.spacing(2, "=", len(to_print))
    print(to_print)
    danimo.spacing(1, ".", len(to_print)//2)

# danimo.spacing(1, ".", 33)
# Renamed (with REFACTOR) "spacing" to "spaces" and "spacing2" to "spacing"
# in danimo.py and auto-updated here!!!
# However, does NOT work for commented-out code, hard-coded strings, etc!!!



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
        # a_reversed.append(a(i))
    return a_reversed

a_test1 = [1, 2, 3]
print(reverseArray(a_test1))




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

main_2()
