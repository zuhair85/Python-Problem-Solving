# Goal: Given a paragraph of text, count how many times each word appears, ignoring uppercase/lowercase differences and punctuation.

import string

def word_frequency_counter(text):
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, " ")
    word_list = text.split()
    dct = {}
    for word in word_list:
        if word not in dct:
            dct[word] = 1
        else:
            dct[word] += 1

    return dct
text = "python is great. python is fun!"

print(word_frequency_counter(text))