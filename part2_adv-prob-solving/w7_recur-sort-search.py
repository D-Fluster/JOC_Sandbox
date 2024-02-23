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

spacing(1, "=", 33)



# names = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]

# using zip() to map values
# mapped = zip(names, roll_no)
# print(mapped)               # <zip object at 0x000002827C72D8C0>



# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = ['x', 'y', 'z']
# zipped = zip(list1, list2, list3)
# # print(zipped)
# result = list(zipped)
# # print(result)
# stringy = "".join(result)
#     # TypeError: sequence item 0: expected str instance, tuple found
# stringy2 = "".join(zipped)
# print(stringy2)



# def ink(some, thing):
#     if thing == "hello":
#         return False
#
#     something = some // 2
#
#     if something == 4:
#         return True
#
#     return False
#
# print(ink(8, "nor hello"))



# print(print("2rly"))
#     # Prints the inner statement, THEN None
#     # 2really
#     # None



# stringz = "hello there"
# print(stringz[0])       # h
# print(stringz[1:])      # ello there



def summy(n):
    if n < 0:
        return None
    elif n == 0:        # Without this, summy(0) returns None
        return 0
    elif n == 1:        # Infinite loop without this
        return 1
    elif n > 1:
        return n + summy(n-1)

def sajak_loop(string):
    vowel_count = 0
    vowels_list = ["a", "e", "i", "o", "u"]

    for char in string:
        if char.lower() in vowels_list:
            vowel_count += 1

    return vowel_count

def sajak_rec(string):
    vowels_list = ["a", "e", "i", "o", "u"]
    if string == "":
        return 0
    elif string[0].lower() in vowels_list:
        return 1 + sajak_rec(string[1:].lower())
    else:
        return 0 + sajak_rec(string[1:].lower())

# def fibonacci(n):
#     sequence = [0]
#     if n == 0:
#         # sequence.append(0)
#         return sequence
#         # elif n == 1:
#     #     return  1, fibonacci(0)
#     elif n >= 1:
#         # new = n + sequence[-1]
#         # sequence.append(n)
#         sequence.append(n + sequence[-1])
#         sequence.extend(fibonacci(n-1))
#         return sequence
#             # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
#             # [n, summy(n-1)]           # works
#             # [n, n + fibonacci(n - 1)] # no output for n>1

        # new = fibonacci(n-1) + sequence[-1] # + sequence[-2]
        # sequence.extend(new)
        # #
        # # new = n + sequence[-1]
        # # sequence.append(n)
        # sequence.append(n + sequence[-1])
        # sequence.extend(fibonacci(n-1))
#
#     # 0: [0]
#     # 1: [0, 1, 0]
#     # 5: [0, 5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
#     # 11: [0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

# seq1 = []
# seq2 = seq1.append("x")
# print(seq2)
# print(seq1.append("x"))
#
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# print(fruits)   # Original fruits
# samp = fruits.append(cars)
# print(fruits)   # Fruits with cars appended (list in list) or extended (same list)
# print(cars)
# print(samp)     # None

def fibonacci(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    elif n > 1:
        sequence = fibonacci(n-1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# WORKS!
# def fibonacci_v1(n):
#     sequence = [0, 1]
#     if n <= 1:
#         return sequence
#     elif n > 1:
#         sequence = fibonacci(n-1)
#         sequence.append(sequence[-1] + sequence[-2])
#         return sequence

def fibonacci_DrEm(n):
    if n == 1 or n == 0:
       return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main3():
    print("Testing extra recursion practice problems 1 of 3")
    spacing(0, "=", 11)

    print("Testing sum(n):")
    spacing(0, "=", 11)
    print("sum of -11: ", summy(-11))   # None
    print("sum of 0: ", summy(0))       # 0
    print("sum of 1: ", summy(1))       # 1
    print("sum of 11: ", summy(11))     # 66
    spacing(1, "-", 33)

    string1 = "hello how are you"
    string2 = "HELLO HOW ARE YOU"
    string3 = "HeLlO hOw ArE yOu abcde"

    print("Testing sajak_loop(string)")
    spacing(0, "=", 11)
    print(f"string1 = {string1}: {sajak_loop(string1)}")
    print(f"string2 = {string2}: {sajak_loop(string2)}")
    print(f"string3 = {string3}: {sajak_loop(string3)}")
    spacing(1, "-", 33)

    print("Testing sajak_rec(string)")
    spacing(0, "=", 11)
    print(f"string1 = {string1}: {sajak_rec(string1)}")
    print(f"string2 = {string2}: {sajak_rec(string2)}")
    print(f"string3 = {string3}: {sajak_rec(string3)}")
    spacing(1, "-", 33)

    print("Testing fibonacci(n)")
    spacing(0, "=", 11)
    print("0: ", fibonacci(0))
    print("1: ", fibonacci(1))
    print("5: ", fibonacci(5))
    print("11: ", fibonacci(11))
    print("33: ", fibonacci(33))
    spacing(1, "-", 33)

    print("Testing fibonacci_DrEm(n)")
    spacing(0, "=", 11)
    print("0: ", fibonacci_DrEm(0))
    print("1: ", fibonacci_DrEm(1))
    print("5: ", fibonacci_DrEm(5))
    print("11: ", fibonacci_DrEm(11))
    print("33: ", fibonacci_DrEm(33))

# main3()

spacing(1, "=", 33)

def fun_function(t):
    if t < 1:
        return
    print("Recursive ", t, "... ")
    fun_function(t-1)
    print(" ...", t, " function")

def hello(string):
    if len(string) <= 0:
        return
    print("hello " + string[0])
    hello(string[1:])

def pascal(r, c):
    if c == 0:
        return 1
    if r == 0:
        return 0
    return pascal(r-1, c) + pascal(r-1, c-1)

def x(n):
    if n < 1:
        return 1
    return n * x(n/2)

def main4():
    print("Testing extra recursion practice problems 2 of 3")
    spacing(0, "=", 11)

    print("Testing fun(t=5):")
    spacing(0, "=", 11)
    print(fun_function(5))
    spacing(1, "-", 33)

    print("Testing hello(string='there'):")
    spacing(0, "=", 11)
    print(hello("there"))
    spacing(1, "-", 33)

    print("Testing pascal(r=3, c=2):")
    spacing(0, "=", 11)
    print(pascal(3,2))
    spacing(1, "-", 33)

    print("Testing x(n=16):")
    spacing(0, "=", 11)
    print(x(16))
    spacing(1, "-", 33)

main4()



def pow_loop(n, p):
    total = 1
    for i in range(p):
        total *= n
    return total

def pow_rec(n, p):
    if p == 1:
        return n
    else:
        return n * pow_rec(n, p-1)

def pyramid(n):
    string = ""
    if n == 1:
        string += "+"
    if n > 1:
        string += f"{n * pyramid(n-1)} \n"
    return string

# 2 * print("a")        # Just prints "a"

def pyramid_loop(n):
    # Works as expected without calling print
    for i in range(1, n+1):
        print("+" * i)
#
#     val = 0
#     for i in range(1, n+1):
#         val += "+" * i
#     print(val)
#
# print(pyramid_loop(5))
# pyramid_loop(10)

def main5():
    print("Testing extra recursion writing practice problems:")
    spacing(0, "=", 11)

    print("Testing pow_loop(n,p):")
    spacing(0, "=", 11)
    print("n=2, p=6: 2^6 = ", pow_loop(2, 6))
    print("n=3, p=4: 3^4 = ", pow_loop(3, 4))
        # Note printing two spaces after ":" -- one hard-coded, one due to the ","
    spacing(1, "-", 33)

    print("Testing pow_rec(n,p):")
    spacing(0, "=", 11)
    print("n=2, p=6: 2^6 = ", pow_rec(2, 6))
    print("n=3, p=4: 3^4 = ", pow_rec(3, 4))
    spacing(1, "-", 33)

    print("Testing pyramid: FAILS")
    spacing(0, "=", 11)
    print("n=5: \n", pyramid(4))

main5()





def both(n):
    print(n, "entry")
    if n == 0:
        return
    else:
        both(n-1)
    print(n, "exit")

def challenge(s):
    x = 0
    if len(s) == 0:
        return x
    elif s[0] == "5":
        x = 1
    return x + challenge(s[1:])

def main6():
    print("Testing extra recursion practice problems 3 of 3")
    spacing(0, "=", 11)

    print("Testing both(n=5):")
    spacing(0, "=", 11)
    both(5)
    spacing(1, "-", 33)

    print("Testing challenge(s='35568515'):")
    spacing(0, "=", 11)
    print(challenge('35568515'))

main6()