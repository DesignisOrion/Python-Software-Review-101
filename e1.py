# Example 1 - Common Design Mistakes

# Program Goal, print a list of words delimeted by commas

# Solution 1 - What's wrong?
list_of_words = ["hello", "yes", "goodbye", "last"]
print(list_of_words[0] + "," + list_of_words[1] +
      "," + list_of_words[2] + "," + list_of_words[3])


# Yes the code works, but what can be improved?
# (1): If we add another word to the list it won't display.
# (2): What if I wanted to change the commas and wanted to do periods?
#       We would have to change every comma.
# End result: This isnt a good design. we want to make it where it could scale flexable.
