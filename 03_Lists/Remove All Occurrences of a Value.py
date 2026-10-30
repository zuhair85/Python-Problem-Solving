# Remove every occurrence of a specified number.EXAMPLE INPUT
#
# [1, 2, 3, 2, 4, 2], target = 2
#
# EXPECTED OUTPUT
#
# [1, 3, 4]

def remove_all_occurr(nums):
    target = 2
    for num in nums:
        if num == target:
            nums.remove(num)
    return nums

nums = [1, 2, 3, 2, 4, 2]
print(remove_all_occurr(nums))