# Example 2 : What is wrong ?


list_of_words = ["hello", "yes", "goodbye", "last", "hello"]
to_print = ""

# for i in range(4):
# To make it more scalable, use this maybe, but issue with adding a comma for output.
for i in range(len(list_of_words)):
    to_print += list_of_words[i]

    # if i != 3:
    if i != len(list_of_words) - 1:
        to_print += ","

print(to_print)


# same issues occuring. The range is hardcoded. Even when adding another word to the list it still will not give the output of hello.

# This is still complexed however.
