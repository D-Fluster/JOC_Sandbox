import danimo
# How to get this to work?

spacing(2, 22)

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
'''



# string_list = ["hello", "how", "you"]
# string_list.insert(2, "are")
# print(string_list)      # ['hello', 'how', 'are', 'you']



