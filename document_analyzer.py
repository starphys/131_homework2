def list_top_values(dictionary, count):
    list_to_return = []

    for i in range(count):
        highest = max(dictionary, key=dictionary.get)
        list_to_return.append(f"{highest}: {dictionary[highest]}")
        del dictionary[highest]

    return list_to_return


def lexographical_sort_dictionary(dictionary):
    sorted_keys = sorted(dictionary, key=str.lower)
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = dictionary.get(key)
    return sorted_dict


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

word_dict = lexographical_sort_dictionary(word_dict)

top_words = list_top_values(word_dict, 5)

print()
for i in range(0, len(top_words)):
    print(top_words[i])
