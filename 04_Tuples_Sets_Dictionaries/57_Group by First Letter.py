# Task: Given a list of words, group them into a dictionary where each key is the first letter of the words, and each value is a list containing all words that start with that letter.

def group_by_first_letter(words):
    dct = {}
    for word in words:
        if word[0] not in dct:
            dct[word[0]] = [word]
        else:
            dct[word[0]].append(word)
    return dct

words = ["apple", "ant", "banana", "ball", "cat", "car", "avocado"]
print(group_by_first_letter(words))