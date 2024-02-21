# 2024 Danielle K. Fluster
# Joy of Coding Academy
# Part 2 - Advanced Problem Solving
# Week 7 - Recursion, Sorting & Searching

from danimo import *

spacing(1, "*", 55)
problem1 = "Read & Predict Recursion"
print(problem1)
spacing(1, "=", len(problem1) // 2)


def gee(n):
    print(n, "...")
    if n == 0:
        return
    else:
        gee(n - 1)


def aich(n):
    if n == 0:
        return
    else:
        aich(n - 1)
    print(n, "...")


def main1():
    gee(10)
    spacing(0, "-", 22)
    aich(10)


main1()


def summer(n):
    x = 1
    if n == 1:
        return x
    else:
        return n + summer(n - 1)


# for i in range(5):
#     print(sum(i))
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

def multiply(a, b):
    x = 1
    if a == 1 and b == 1:
        return x
    elif a == 1:
        return b
    else:
        return b + multiply(a - 1, b)


def sum_of_squares(n):
    x = 1
    if n == 1:
        return x
    else:
        return n ** 2 + sum_of_squares(n - 1)


def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def main2():
    print(summer(5))
    print(5 + 4 + 3 + 2 + 1)
    print()
    print(multiply(2, 3))
    print(multiply(5, 2))
    print(multiply(4, 3))
    print(multiply(1, 2))
    print(multiply(2, 1))
    print()
    print(sum_of_squares(3))
    print(sum_of_squares(5))
    print(sum_of_squares(7))
    print()
    print(reverse("Happy Friday!"))
    print(reverse("Mississippi"))
    print(reverse("I"))
    print(reverse(" "))


main2()



spacing(3, "*", 33)
# print(9//2)

minT = 2
maxT = 3
midT = minT + (maxT - minT) // 2
print(midT)

spacing(1, "_", 33)



names = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

# using zip() to map values
# mapped = zip(names, roll_no)
# print(mapped)               # <zip object at 0x000002827C72D8C0>



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
# print(zipped)
result = list(zipped)
# print(result)
stringy = "".join(result)
    # TypeError: sequence item 0: expected str instance, tuple found
stringy2 = "".join(zipped)
print(stringy2)
