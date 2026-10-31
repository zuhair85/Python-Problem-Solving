# Goal: Determine whether two strings are anagrams of each other. Two strings are anagrams if they contain exactly the same characters, with each character appearing the same number of times, regardless of the order.
# Method 1: Using sorting. This is probably the easiest approach to understand.
# Python has a built - in function called sorted().
#
# It takes an iterable and returns a new sorted list.
#
# Example:word1 = "listen"
# word2 = "silent"
# print(sorted(word1) == sorted(word2))

# Method 2: Using Dictionaries

def anagram_checker(word1, word2):
    dct1 = {}
    # dct2 = {}
    for c1 in word1:
        if c1.isalpha():
            if c1 not in dct1:
                dct1[c1] = 1
            else:
                dct1[c1] += 1
    for c2 in word2:
        # if c2.isalpha():
        #     if c2 not in dct2:
        #         dct2[c2] = 1
        #     else:
        #         dct2[c2] += 1
        if c2 not in dct1:
            return False
        if c2.isalpha() and c2 in dct1:
            dct1[c2] -= 1
    for value in dct1.values():
        if value != 0:
            return False
    return True



word1 = 'banana'
word2 = 'aaabnn'
print(anagram_checker(word1,word2))
