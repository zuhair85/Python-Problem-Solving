# Given a list of numbers, calculate their sum without using sum().EXAMPLE INPUT
#
# [10, 20, 30, 40, 50]
#
# EXPECTED OUTPUT
#
# 150

def addall(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
nums = [10, 20, 30, 40, 50]
print(addall(nums))