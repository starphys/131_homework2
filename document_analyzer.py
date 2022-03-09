import re


def list_top_values(dictionary, count):
    list_to_return = []

    for i in range(count):
        highest = max(dictionary, key=dictionary.get)
        list_to_return.append(highest)
        list_to_return.append(dictionary[highest])
        del dictionary[highest]
    return list_to_return


# Get all the text from a file into one string
with open("document.txt") as doc:
    lines = doc.read()

# Get every word from the string into a list
# Note: contractions will separate with this approach
word_list = lines.split()

if word_list == None:
    print("File was empty.")
    quit()

# Iterate through list, assign unique values to dictionary, increment repeats
word_dict = {}
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1

top_words = list_top_values(word_dict, 5)

print()
for i in range(0, len(top_words), 2):
    print(f"{top_words[i]}: {top_words[i+1]}")
