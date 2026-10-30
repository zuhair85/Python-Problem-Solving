# Count how many times a given value appears without count().EXAMPLE INPUT
#
# [1, 2, 2, 3, 2, 4], target = 2
#
# EXPECTED OUTPUT
#
# 3

def count_ocurr(nums):
    count = 0
    target = 2
    for num in nums:
        if num == target:
            count += 1
    return count

nums = [1, 2, 2, 3, 2, 4]
print(count_ocurr(nums))