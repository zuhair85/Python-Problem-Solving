# Task: Given two dictionaries, merge them into a single dictionary. If a key exists in both dictionaries, add their values together. If a key exists in only one dictionary, keep its original value.

def dictionary_merge(dct1, dct2):
    for key,value in dct2.items():
        if key not in dct1:
            dct1[key] = dct2[key]
        else:
            dct1[key] = dct1[key] + dct2[key]

    return dct1

dct1 = {
    'apple': 10,
    'banana': 20,
    'orange': 15
}

dct2 = {
    'banana': 5,
    'orange': 10,
    'grape': 25
}

# dct1 = {'a': 10, 'b': 20}
# dct2 = {'b': 5, 'c': 15}
# dct1 = {}
# dct2 = {'a': 10}

print(dictionary_merge(dct1,dct2))