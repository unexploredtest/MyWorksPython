# How to write on a text:
with open('Information/SomeNumbers.txt', 'w') as TextW:
    TextW.write("I don't know what to write.")
    # To continue writing in another line:
    TextW.write("\nAny ideas?")

# If you wanted to add lines after closing the text, but don't
# want to delete the previous work, then instead of "w", use "a":

with open('Information/SomeNumbers.txt', 'a') as W:
    W.write("\nI don't have any Idea either.")

# If you wanted to write lists:
Numbers = ["\nHow you're doing?", "\nI don't know",
"\nGoodbye.", "\nFinished."]

with open('Information/SomeNumbers.txt', 'a') as TextA:
    TextA.writelines(Numbers)
