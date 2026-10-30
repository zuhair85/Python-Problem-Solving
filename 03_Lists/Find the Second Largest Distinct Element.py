# Find the second largest distinct number without sorting.EXAMPLE INPUT
#
# [10, 20, 4, 45, 99, 99]
#
# EXPECTED OUTPUT
#
# 45

def find_second_largest(nums):
    largest = nums[0]
    second_largest = None

    if not nums:
        return None

    for num in nums:
        if second_largest == None:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest:
                second_largest = num

        else:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and num > second_largest:
                second_largest = num

    return second_largest

nums = [10, 20, 4, 45, 99, 99]
#nums = [-10, -20, -5, -30]
print(find_second_largest(nums))