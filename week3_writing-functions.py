# Day 1
# Mods 1-3


# def addFromLecture(x ,y):
#     print(f"I will add the numbers {x} and {y}")
#     return x + y
#
# sum = addFromLecture(55, 777)
# print("=", sum)


'''
def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}. Wow!")

# add(1,2)
# print("")
# add(4, 16)
# print("")
# print("")


def multiply(a, b):
    print(f"The product of {a} and {b} is {a * b}. Amazing!")

# multiply(1, 2)
# print("")
# multiply(3, 4)


def main():
    a = int(input("Enter any integer: "))
    b = int(input("Enter another iteger: "))
    add(a, b)
    print("AND")
    multiply(a, b)

main()
'''


''''''


'''
# Day 1
# Mod 4

def f(x):
    x = x - 1
    return g(x) + 1

def g(x):
    return x * 2

def h(x):
    if x%2 == 1:
        return f(x) + x
    else:
        return f(f(x))

test1 = 4
test2 = 5

print(h(test1))
print("")
print(h(test2))
print("")
print(h(3))
'''


''''''


'''
# Day 1
# Mod 6
# Recursion

# Factorial without recursion:
def factorial_iterative(n):
    product = 1
    for i in range (2, n+1):
        product *= i
    return product

# print(factorial_iterative(5))
# print("")

# Factorial with recursion:
def factorial_recursive(n):
    if n == 1:                  # A *base* case is required and should be written first
        return 1
    else:
        return n * factorial_recursive(n-1)     # The *recursive* case

# print(factorial_recursive(5))
# print("")

# print(factorial_iterative(3) == factorial_recursive(3))
# print("")
# print("")
# print("")



# Adding numbers 1 thru n iteratively:
def add_itr(n):
    sum_itr = 0
    for i in range(n+1):
        sum_itr += i
    return sum_itr

print("Adding Iteratively 2, 3, 4 & 5")
print(add_itr(2))
print(add_itr(3))
print(add_itr(4))
print(add_itr(5))
print("")

def add_rec(n):
    if n == 1:
        return 1
    else:
        return n + add_rec(n-1)

print("Adding Recursively 2, 3, 4 & 5")
print(add_rec(2))
print(add_rec(3))
print(add_rec(4))
print(add_rec(5))
print("")

print("Checking Equality for 7, 21, 55 & 111")

def add_equal(n):
    return add_itr(n) == add_rec(n)

print(add_equal(7))
print(add_equal(21))
print(add_equal(55))
print(add_equal(111))
'''


''''''


'''
# Day 1
# Mod 7
# Reading Functions

def double(x):
    return 2 * x

def quad(x):
    return double(double(x))

def hello(name):
    print("Hello", name + ", how are you today?")

def repeat (string, n):
    return string * n

def square(string, n):
    for i in range(n):
        print(repeat(string, n))

print(double(5))        # 10
print("")
print(quad(4))          # 16
print("")
hello("Joe")            # Hello Joe, how are you today?
print("")
print(repeat("hi", 10))
print("")
square("*", 4)



# Day 2
# Writing Functions
# "Header"

def header(text, surround):
    surrounding = surround * (len(text) + 4)
    print(surrounding)
    # print(surround, text, surround)
    print(f"{surround} {text} {surround}")
    print(surrounding)
    print("")

def main():
    header("Hello, World!", "*")
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")
    header("We Will, We Will Rock You", "~")

main()



# Day 2
# Writing Functions
# "Pyramid"

def pyramid(char, num):
    for i in range(1, num + 1):
        print(char * i)
    print("")

def main():
    pyramid("*", 2)
    pyramid("+", 5)
    pyramid("x", 10)

main()



# Day 2
# Writing Functions
# "Absolute Difference"

# Diff 5 & 10 = 5
# Diff 10 & 5 = 5
# Diff -200 & 200 = 400

# x = 5
# y = 10

def abs_diff(x, y):
    if x == y:
        return 0
    elif x > y:
        return abs(x - y)
    else:
        return abs(y - x)

def main():
    print(abs_diff(5, 10))
    print(abs_diff(10, 5))
    print(abs_diff(200, -200))
    print(abs_diff(-200, 200))

main()



# Day 2
# Writing Functions
# "Is Even"

def is_even(num):
    if num%2 == 0:
        print(f"Yes, the number {num} is even!")
    else:
        print(f"No, the number {num} is not even; it is odd. Like me.")

def main():
    for i in range(-1, 4, 1):
        is_even(i)

main()



# Day 2
# Writing Functions
# "Calculate Total"

def calc_tot(meal, tax_rate, tip_rate):
    mealTax = meal * tax_rate
    mealTip = meal * tip_rate
    mealTotal = round((meal + mealTax + mealTip), 2)
    return mealTotal

meal = 53.48
tax_rate = 0.07
tip_rate = 0.18

print(f"${calc_tot(meal, tax_rate, tip_rate)}")

# tot_base = meal * (1 + tax_rate) * (1 + tip_rate)
# tot_baseR = round(tot_base, 2)
# print(f"${tot_baseR}")          # $67.52, but should be $66.85
#
# tot_tip1st = (meal * (1 + tax_rate)) + (meal * tip_rate)
# tot_tip1stR = round(tot_tip1st, 2)
# print(f"${tot_tip1stR}")
'''


# Day 2
# Writing Functions
# "Hey" / "There" / "Are We"

def hey(n):
    return n * n            # or "n**2" or "pow(n, 2)"

def there(n):
    if n >= 0:
        return 2**n         # "2^5" is written as "2**5" or "pow(2,5)" in Python
    else:                   # The "else" here is OPTIONAL b/c of the semantics!
        return 0

def are_we(repeat, phrase):
    print(f"Are we {phrase} yet? " * repeat)

def main():
    print(hey(5))
    print(hey(0))
    print(hey(-3))
    print("---")
    print(there(5))
    print(there(0))
    print(there(3))
    print(there(-2))
    print(there(-6))
    print("---")
    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")

main()

