# Given N distinct integers from 0 through N with one missing, identify the missing integer.
#
# Suppose you have a list:
# numbers = [3, 0, 1]
# The complete range should contain the numbers 0, 1, 2, and 3.
#
# Since 2 is missing, your expected output is: 2

# Method 1: Use a loop (beginner-friendly)
# Try solving this without using sets or advanced techniques.
#
# Hints:
# 1. The list contains N numbers, so the complete range is 0 through N, inclusive.
# 2. Use a loop to check each integer in that range.
# 3. Check whether each integer exists in numbers.
# 4. If an integer doesn't exist, you've found the missing number.

def find_missing_number(lst):
    for x in range(0, len(lst) + 1):
        if x not in lst:
            return x
lst = [3, 0, 1, 5, 6, 2]
print(find_missing_number(lst))

# Method 2: Use the mathematical formula
#
# There's a more efficient way that avoids repeatedly searching the list.
#
# The sum of all integers from 0 through N is:
#
# S = N(N+1)/2
#
# For example, if N = 3:
#
# S = 3(3+1)/2 = 6
#
# The complete range is 0 + 1 + 2 + 3 = 6.
# Your actual list is [3, 0, 1], whose sum is 4.
#
# Therefore:
# Missing number = S - Actual sum
# = 6 - 4 = 2
#
# Python provides the built-in sum() function, which can calculate the actual sum of your list.

def find_missing_number(lst):
    N = len(lst)
    S = int((N * (N+1)) / 2)
    return S - sum(lst)

lst = [0, 1, 2, 4, 5]
print(find_missing_number(lst))