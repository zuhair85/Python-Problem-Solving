# Goal: Given a list of integers and a target number, find the indices of two elements whose sum equals the target.
# Suppose you have:
# numbers = [2, 7, 11, 15]
# target = 9
# You need to find two numbers that add up to 9.
#
# Since (2 + 7 = 9), the answer is:
# [0, 1]

def two_sum(numbers, target):
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if numbers[x] + numbers[y] == target and x != y:
                return f'({x}, {y})'

numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))