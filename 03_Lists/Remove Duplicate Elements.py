# Remove duplicates while preserving the original order, without using set().EXAMPLE INPUT
#
# [1, 2, 2, 3, 4, 4, 5]
#
# EXPECTED OUTPUT
#
# [1, 2, 3, 4, 5]

def remove_dups(nums):
    uniqs = []
    for num in nums:
        if num not in uniqs:
            uniqs.append(num)
    return uniqs

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_dups(nums))