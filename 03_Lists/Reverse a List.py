# Reverse a list without using reverse() or slicing.EXAMPLE INPUT
#
# [1, 2, 3, 4, 5]
#
# EXPECTED OUTPUT
#
# [5, 4, 3, 2, 1]


# Method 1: The Two-Pointer Approach (In-Place, O(1) Space)
#
# This method swaps elements from the outside in using a left and right pointer until they meet in the middle.
# It modifies the original list directly, which is the most memory-efficient solution
#
# def reverse_in_place(lst):
#     left = 0
#     right = len(lst) - 1
#
#     while left < right:
#         # Swap the elements
#         lst[left], lst[right] = lst[right], lst[left]
#         # Move pointers toward the center
#         left += 1
#         right -= 1
#     return lst
#
# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# print(reverse_in_place(my_list))  # Output: [5, 4, 3, 2, 1]



# Method 3: The pop() and insert() Approach (Alternative In-Place)
#
# A clever alternative discussed on tech channels like GeeksforGeeks and demonstrated in various Python tutorials involves shifting elements forward.
# You can loop through the length of the list, continuously popping the last element and inserting it at the current index i.
#
def reverse_with_pop(lst):
    for i in range(len(lst) - 1):
        # Remove the last item and insert it at the current index
        lst.insert(i, lst.pop())
    return lst

# Example usage:
my_list = [10, 20, 30, 40]
print(reverse_with_pop(my_list))  # Output: [40, 30, 20, 10]
