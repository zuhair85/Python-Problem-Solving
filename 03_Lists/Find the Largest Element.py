# Find the largest number without using max().EXAMPLE INPUT
#
# [12, 45, 7, 89, 23]
#
# EXPECTED OUTPUT
#
# 89

def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num >= largest:
            largest = num
    return largest

nums = [12, 45, 7, 89, 23]
print(find_largest(nums))