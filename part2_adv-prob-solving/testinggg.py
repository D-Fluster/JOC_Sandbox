# Adding new directory to JOC_Sandbox


# Assume the user enters the following:
# hello goodbye cat dog DONE done
list = []
prompt = "Please enter word, ‘done’ to finish "
response = input(prompt)
while response != "done":
    list.append(response)
    response = input(prompt)
print(sorted(list))
print(sorted(list))