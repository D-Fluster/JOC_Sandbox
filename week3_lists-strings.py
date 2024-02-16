import danimo
# How to get this to work?

# from danimo import spacing
# danimo.spacing(2, 22)
# danimo.lines(5)

'''
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
'''
Good idea to initialize with an empty function or "STUB" such as:

def mangle(str):
    return str
'''
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

spacing(2, 22)



# Day 4
# Reading "While"s

# a - verified
print("= = = = =")
print("Basic While: #a")
print("===")

j = 4
ans_while = []
while j > -4:
    print(j)
    ans_while.append(j)
    j -= 1
print("---")

ans_for = []
for j in range(4, -4, -1):
    print(j)
    ans_for.append(j)
print("---")

print(f"For & While Loops Equivalent? {str(ans_while == ans_for).upper()}")
# print(ans_while)
# print(ans_for)
print("= = = = =")



# b -- verified
print("= = = = =")
print("Basic While: #b")
print("===")

# print(2, "str")           # Does print "2 str" (no quotes anywhere)

# def while_b_given():

string = "Hello"
builder = ""
i = 0
while i < len(string):
    builder += string[i].swapcase()
    print(i, builder)
    i += 1
print(string, "->", builder)

string = "Hello"
builder = ""
for i in range(len(string)):
   builder += string[i].swapcase()
   print(i, builder)
print(f"{string} -> {builder}")



# c
x = 0
i = 1
while x < 20:
    if x > 5:
        x += 15
    else:
        x += 1
    print(i, x)
    i += 1
print("---")

# NOT EQUIVALENT!!!
x = 0
for i in range(1, 20):
   if x > 5:
      x += 15
      # i += 14
   else:
      x += 1
   print(i, x)

print(x):
hell{""}



# string_list = ["hello", "how", "you"]
# string_list.insert(2, "are")
# print(string_list)      # ['hello', 'how', 'are', 'you']



# Day 4
# Combining "While"s

# a -- in progress

string = "HELLO"
x = 0
while string[x] != "L":
    print(string[x], end="... ")
    x += 1
print("\n", string, "first L is at", x)
    # By itself, skips a line (due to the \n) AND adds a space (due to the ,)

# print(sorted(["ab", "a", "abc", "x"]))
# Yes, prints ['a', 'ab', 'abc', 'x']



# b -- verified
list = []
prompt = "Please enter word, or type ‘done’ to finish: "
response = input(prompt)
while response != "done":
    list.append(response)
    response = input(prompt)
print(sorted(list))



# c -- verified

# print(1%2)      # 1 for odd
# print(2%2)      # 0 for even
# print(0%2)      # 0 for 0

x = 0
while x < 20:
    if x > 5:
        if x % 2 == 0:
            x *= 2
        else:
            x *= -1
    else:
        x += 10
    x += 1
print(x)

# Yes! It IS 25, woo hoo!



# Day 4
# Writing Whiles, Part 1

# 1-a: verified
# var = 1
# while var < 6:
#    print(var)
#    var += 1

# 1-b: verified
# n = 2
# while n < 12:
#     print(n)
#     n += 3

# 1-c: verified
# num = -10
# while num <= 0:
#    print(num, end=" ")
#    num += 2

# 1-d: verified
# chars = 1
# while chars <= 4:
#    print("*" * 4)
#    chars += 1         # Almsot forgot this & went infinite!

# 2: verified
# str = "CSCI 150"
# len_cur = 0
# len_fin = len(str)
# while len_cur < len_fin:
#     print(str[len_cur])
#     len_cur += 1

# 3: Create a program that allows the user to enter in a list of numbers,
# prints them out in sorted order, and prints the sum and average of
# the numbers. Prompt the user to continue entering numbers, and
# enter the number ‘0’ when finished.

user_prompt = "Please enter any number (to quit, enter '0'): "
user_list = []
user_response = int(input(user_prompt))

while user_response != 0:
    user_list.append(user_response)
    user_response = int(input(user_prompt))

user_list_sum = 0
user_list_len = len(user_list)
for i in range(user_list_len):
    user_list_sum += user_list[i]
user_list_avg = user_list_sum / user_list_len

print(f"\nThank you for your valued feedback! \n"
      f"You entered the following numbers: {sorted(user_list)}. \n"
      f"The sum of these numbers is {user_list_sum}, \n"
      f"and their average value is {user_list_avg}.")

print

# But why doesn't this version work???
# # user_input = input("Please enter any number (to quit, enter '0'): ")
# # user_list = []
# # # val_cur = user_input
# # while user_input != 0:
#     user_list.append(int(user_input))
    # val_cur = user_input
    # Infinite loop -- see
    # print(user_list)
'''


# Day 4
# Writing Whiles, Part 2

# 1: average_neg_evens:
# avg_neg_ev_list = []

def average_neg_evens_FOR(list):
    list_neg_evens = []
    for i in range(len(list)):
        if list[i] < 0:
            if list[i]%2 == 0:
                list_neg_evens.append(list[i])
    avg = sum(list_neg_evens) / len(list_neg_evens)
    return avg


def average_neg_evens_WHILE(list):
    list_neg_evens = []
    i = 0
    while i < len(list):
        if list[i] < 0:
            if list[i]%2 == 0:
                list_neg_evens.append(list[i])
        i += 1
    avg = sum(list_neg_evens) / len(list_neg_evens)
    return avg


# 2: count_letter

def count_letter_FOR(list, string):
    count = 0               # Initializing aggregator variable
    # list = list.upper()   # Doesn't work like that
    for i in range(len(list)):
        # list[i] = list[i].upper()       # Converting each word on the list to uppercase
        for j in range(len(list[i])):
            if list[i][j].upper() == string.upper():
                # print(list[i][j].lower(), i, j)
                count += 1
    return count



def count_letter_WHILE(list, string):
    count = 0
    i = 0
    while i < len(list):
        list[i] = list[i].upper()
        string = string.upper()
            # PRO TIP: More efficient to initalize before loop,
            # as it'll be used in the same form over & over
        count += list[i].count(string)
            # Not as DRY, but could technically do
            # list[i].upper().count(string.upper()) all at once
        i += 1
    return count


    # WHY DOESN'T THIS WORK...?!!??!!?
    # count = 0
    # i = 0
    # j = 0
    # while i < len(list):
    #     while j < len(list[i]):
    #         if list[i][j].upper() == string.upper():
    #             print(list[i][j].lower(), i, j)
    #             count += 1
    #         j += 1
    #     i += 1
    # return count


    # count = 0           # Initializing aggregator variable
    # i = 0               # Initializing loop variables
    # j = 0
    # # string = string.upper()
    # # list = list.upper()
    # while i < len(list):
    #     sublist = list[i].upper()
    #     # list[i] = list[i].upper()       # Converting each word on the list to uppercase
    #     # if string.upper() in list[i].upper():
    #     #     count += 1
    #     # i += 1
    #     while j < len(sublist):
    #         if sublist[j] == string.upper():
    #             count += 1
    #             print(sublist[j], i, j)
    #         # else:
    #         #     count += 0
    #         j += 1
    #     i += 1
    # # print(count)
    # return count

def testing_whiles():
    countList = ["HELLO", "goodbye", "1234 Oooh!"]
    print(countList[0][0].upper() == "h".upper())   # True
    danimo.spaces(0, 5)
    print(count_letter_FOR(countList, "o"))
    danimo.spaces(0, 5)
    print(count_letter_WHILE(countList, "o"))
    danimo.spaces(0, 5)
    print(countList[1][-1] == "E")
    danimo.spaces(0, 5)
    print(len(countList[0]))
    print(len(countList[1]))
    print(len(countList[2]))
    danimo.spaces(0, 5)

# testing_whiles()

def main_whiles():
    average_neg_evens_list = [0, 1, 2, -2, -3, -4, 3, 4]

    print(f"\n=== TESTING Q1: average_neg_evens === \n"
          f"List input: {average_neg_evens_list} \n"
          f"Expected output: -3 \n"
          f"Output using 'for' loop: {average_neg_evens_FOR(average_neg_evens_list)}, \n"
          f"Output using 'while' loop: {average_neg_evens_WHILE(average_neg_evens_list)} \n"
          f"Same? {average_neg_evens_FOR(average_neg_evens_list) == average_neg_evens_WHILE([0, 1, 2, -2, -3, -4, 3, 4]) == -3}")

    danimo.spaces(1, 11)

    count_letter_list = ["HELLO", "goodbye", "1234 Oooh!"]
    counter_letter_string = "o"

    print(f"=== TESTING Q2: count_letter === \n"
          f"List input: {count_letter_list} \n"
          f"String input: {counter_letter_string}"
          f"Expected output: 6 \n"
          f"Output using 'for' loop: {count_letter_FOR(count_letter_list, counter_letter_string)}, \n"
          f"Output using 'while' loop: {count_letter_WHILE(count_letter_list, counter_letter_string)} \n"
          f"Same? {count_letter_FOR(count_letter_list, counter_letter_string) == count_letter_WHILE(count_letter_list, counter_letter_string) == 6}")

main_whiles()