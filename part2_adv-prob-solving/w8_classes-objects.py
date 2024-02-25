from danimo import *

spacing(1, "*", 55)

# 1. Import class implementation

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

def print_all_nodes_v0(head):
    node = head
    while head.next_node is not None:
        print(node)
        node.set_next(head.next_node)

def print_all_nodes_v1(head):
    current_node = head
    while current_node is not None:
        print(current_node)
        current_node = current_node.get_next()      # Inifnite loop
        # current_node = current_node.set_next(head.get_next())     # Prints nothing

# 3. Create a function to print any length of linked list
def print_all_nodes_v2(head):
    current_node = head
    # print(current_node.get_data())
    while current_node is not None:
        print(current_node.get_data(), end=" -> ")
        current_node = current_node.get_next()      # Inifnite loop
        # print(current_node)
        # current_node = current_node.set_next(head.get_next())     # Prints nothing
    # Success! Hello -> 12345 -> Wassup -> 9090909 ->

def main():
    # new_node = Node("First Node Data")
    # next_node = Node("Second Node Data", new_node)
    # print(next_node.get_data())

    # list = []
    # list.append("Hello")
    # list.append(12345)
    # list.append("Wassup")
    # list.append(9090909)
    # # print(list)
    # for i in range(len(list)):
    #     print(list[i], end=" -> ")
    # print_all_nodes_v0(list[0])

    head_node = Node("Hello")
    second_node = Node(12345, head_node)
    third_node = Node("Wassup", second_node)
    fourth_node = Node(9090909, third_node)
    # print_all_nodes_v0(head_node)
    # print_all_nodes_v1(head_node)           # <__main__.Node object at 0x0000024B0EC0E720>
    # print_all_nodes_v2(head_node)
        # Hello ->

    spacing(1, "=", 25)

    # 2. Create a linked list of 4 numbers/strings & print them
    last_node = Node(9090909)
    secToLast_node = Node("Wassup", last_node)
    thirToLast_node = Node(12345, secToLast_node)
    first_node = Node("Hello", thirToLast_node)

    print()
    print("2. Create a linked list of 4 numbers/strings & print them:")
    # print_all_nodes_v0(head_node)       # Inifnite loop
    # print_all_nodes_v1(head_node)       # Returns nothing or <__main__.Node...>
    print_all_nodes_v2(first_node)
        # Almost! OH! Just b/c I was double-printing head & printing the node itself (not ".data") for testing
    # Without end=
        # Hello
        # <__main__.Node object at 0x0000020D1CE22E40>
        # 12345
        # <__main__.Node object at 0x0000020D1CE0E570>
        # Wassup
        # <__main__.Node object at 0x0000020D1CE0E540>
        # 9090909
        # None
    # With end=" -> "
        # Hello -> <__main__.Node object at 0x000002AE0B63BB30>
        # 12345 -> <__main__.Node object at 0x000002AE0B96E5A0>
        # Wassup -> <__main__.Node object at 0x000002AE0B96E570>
        # 9090909 -> None
    print()

    # 4. After printing, remove a node and re-print

    # Removing the last element
    print()
    print("4. After printing, remove a node and re-print:")
    print("4-a. Removing last element:")
    secToLast_node.set_next(None)
    print_all_nodes_v2(first_node)
        # IT WORKS!
        # Hello -> 12345 -> Wassup ->
    print()

    # 5. Add a new node and re-print
    print()
    print("5. Add a new node and re-print:")
    new_first_node = Node(3.14, first_node)
        # Doesn't seem like there's a separate "head" to concretely define here
    print_all_nodes_v2(new_first_node)
        # 3.14 -> Hello -> 12345 -> Wassup ->
    print()

    # Removing another element (12345)
    print()
    print("4-b. Removing another element (thirToLast):")
    first_node.set_next(secToLast_node)
    print_all_nodes_v2(new_first_node)
    # IT WORKS!
    # 3.14 -> Hello -> Wassup ->
    print()

    # secToLast_node = Node("Wassup", last_node)
    # thirToLast_node = Node(12345, secToLast_node)
    # first_node = Node("Hello", thirToLast_node)
    # new_first_node = Node(3.14, first_node)


main()




'''
# Yes, key:value would only work if all data was unique

# But also, dictionaries can hold 2 pieces of information in its value
    # i.e., can hold multiple values keyed to the same thing
# Similar to JSON files -- one item in data needs to be unique,
    # but the rest of it can hold multiple things

'''


# queries = ["abc", "ab", "bc"]
# query_counts = [0 for i in range(len(queries))]
# print(query_counts)


# def arrayManipulation(n, queries):
#     # Write your code here
#
#     array = [0 for i in range(n)]
#
#     for query in queries:
#         a = query[0]
#         b = query[1] + 1
#         k = query[2]
#         print(a, b, k)
#         for i in range(1, n + 1):
#             if i in range(a, b):
#                 array[i - 1] += k
#             print(array)
#
#     print(max(array))
#
# arrayManipulation(5, [[1, 2, 3]])



grades = [73, 67, 38, 33]

for grade in grades:
    # print(grade)
    # print(grade%5)
    if grade in range(38, 101):
        # print(grade)
        if grade%5 >= 3:
            # print(grade)
            grade += grade%5 - 1
            # print(grade) # 75, 40

# print(grades)


def gradingStudents(grades):
    # Write your code here

    # grades_final = grades.copy()

    # for grade in grades:
    #     if grade in range(38, 101):
    #         if grade%5 >= 3:
    #             grade += grade%5 - 1

    for i in range(len(grades)):
        if grades[i] in range(38, 101):
            if grades[i]%5 != 0 and grades[i]%5 >= 3:
                grades[i] += 5 - grades[i]%5

    return grades

print(gradingStudents([x for x in range(101)]))