# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Danielle Fluster
# DISCORD S/N:  LAdanimo
# ASSIGNMENT:   Project 2: Stacks & Queues

# Success! All tests passed @ 2024-02-17 ~8:30am


from StackJOC import Stack

# Returns True if the braces match,
# & False otherwise


# dictionary_new = {"(": ")"}
# print(dictionary_new)
#
# print()
# testing = dictionary_new["("]
# print(testing)
#
# print()
# dictionary_new["["] = "]"
# print(dictionary_new)


braces_dictionary = {"(": ")", "[" : "]", "{" : "}"}

# tester = braces_dictionary["("]
# print(tester)



def matcher(str):
    s = Stack([])
    # FIXME
    # str = "[()]"
    braces_dictionary = {"(": ")", "[" : "]", "{" : "}"}

    # char == braces_closers[0] and s.peek() == braces_openers[0]:

    for char in str:
        if char in braces_dictionary.keys():      # char is looping over only the keys in the dictionary (i.e., open braces)
            s.push(char)                        # Currently only works on empty set -- not pushing to stack as expected
        elif char in braces_dictionary.values() and s.is_empty():                           # If a closed bracket is encountered when
            return False                                                        # the stack is empty, it's unmatched
        elif char in braces_dictionary.values():        # Still need to check if they're matching here -- to peek
            s.pop()

    if s.is_empty():                    # If the full loop runs and the empty stack is returned, all brackets matched
        return True

    else:                               # Otherwise, there are mismatched brackets
        return False



def main():
    print("matcher: ", matcher("][()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

