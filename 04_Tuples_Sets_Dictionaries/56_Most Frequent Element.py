# Task: Given a list of elements, find the element that appears most frequently. Your solution must also handle ties (when multiple elements have the same highest frequency).Task: Given a list of elements, find the element that appears most frequently. Your solution must also handle ties (when multiple elements have the same highest frequency).

def most_freq_ele(lst):
    if not lst:
        return []
    dct = {}
    for item in lst:
        if item not in dct:
            dct[item] = 1
        else:
            dct[item] += 1
    highest = max(dct.values())
    most_ele = []
    for key,value in dct.items():
        if value == highest:
            most_ele.append(key)
    return most_ele
lst = numbers = [1, 2, 2, 2, 3, 3, 3, 4]
print(most_freq_ele(lst))