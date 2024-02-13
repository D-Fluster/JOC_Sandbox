strings = ["abc", "def", "ghi"]
# strings = ['  b n', 'f ete', 'liths', 'astat', 't ene', '  r d']

# longest = 0
# for i in strings:
#     if len(i) > longest:
#         longest = len(i)            # Works
#     # else:
#     #     strings[i].append(" ")
# print(longest)

# for i in strings:
#     if len(i) < longest:
#         strings[i].append("*")      # Doesn't work unless same len
# print(strings)

for word in strings:
    wordElement = strings.index(word)
    for letter in word:
        letterElement = word.index(letter)
        print(strings[letterElement][wordElement], end = "")
    print("")