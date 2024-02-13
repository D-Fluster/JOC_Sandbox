# Day 3
# Using Lists & Strings


# string = "Hello!"
# print(string[2:4])      # ll (i.e., 2nd & 3rd characters)
# print(string[:])        # Hello! (full sequence from 0th to nth)
# print(string[:5])       # Hello (only through 4th character)


def average_of_list(amount):
    list_to_average = []
    for i in range(amount):
        list_to_average.append(int(input("Please enter an integer value: ")))
    mean_of_list = sum(list_to_average) / len(list_to_average)
    print(f"You entered the following numbers: {list_to_average}, "
          f"which have a mean/average value of {mean_of_list}. "
          f"Pretty cool!")

# average_of_list(20)

def mangle(string):
    string = string.upper()
    string1 = string[0:2]            # Inclusive on both ends??
    string2 = string[3:-3]
    string3 = string[-2:]
    # print(f"string1 = {string1}")
    # print(f"string2 = {string2}")
    # print(f"string3 = {string3}")
    # string = string1 + string2 + string3
    print(string1 + string2 + string3)
    # print("---")

'''
Good idea to initialize with an empty function or "STUB" such as:

def mangle(str):
    return str
'''

def proTest():
    mangle("hellothere")
    mangle("42 degrees Celsius")
    mangle("eeeeeee")
    mangle("abcdefg")   # should be ABDFG

# proTest()


def count_e(list):
    num_e = 0
    for word in list:
        for char in word:
            if char == "e" or char == "E":
                num_e += 1
    return num_e

# count_list1 = ["hi", "hello", "EEK!"]
# count_list2 = count_list1 + ["wassup", "eve"]
#
# print(count_e(count_list1))     # 3
# print(count_e(count_list2))     # 5



def count_vowels(list):
    num_vowels = 0
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for word in list:
        for char in word:
            if char in vowels:
                num_vowels += 1
    return num_vowels

print(count_vowels(["hi", "hello", "OOF!"]))    # 5