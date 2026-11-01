# Task: Count the number of words in a sentence, handling extra whitespace.

def word_counter(text):
    count = 0
    new_word = False
    for ch in text:
        if ch.isalpha() and new_word == False:
            new_word = True
            count += 1
        # elif ch.isalpha() and new_word == True:
        #     continue
        elif new_word is True and ch.isalpha() is False:
            new_word = False

    return count

text = "Python is amazing! I love programming."
print(word_counter(text))