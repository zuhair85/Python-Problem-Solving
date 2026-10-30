# Merge two sorted lists into one sorted list without using sort().EXAMPLE INPUT
#
# [1, 3, 5], [2, 4, 6]
#
# EXPECTED OUTPUT
#
# [1, 2, 3, 4, 5, 6]

def sort_list(lst1, lst2):
    sorted_list = []
    i = 0
    j = 0
    while i < len(lst1) or j < len(lst2):
        if i == len(lst1):
            sorted_list.append(lst2[j])
            j += 1
        elif j == len(lst2):
            sorted_list.append(lst1[i])
            i += 1
        elif lst1[i] == lst2[j]:
            sorted_list.append(lst1[i])
            sorted_list.append(lst2[j])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            sorted_list.append(lst1[i])
            i += 1
        elif lst2[j] < lst1[i]:
            sorted_list.append(lst2[j])
            j += 1

    return sorted_list

lst1 = [1, 3]
lst2 = [2, 4, 5, 6]

print(sort_list(lst1,lst2))