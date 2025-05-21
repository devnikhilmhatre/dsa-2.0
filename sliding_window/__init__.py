def max_sub_array(nums: list, k: int):
    i = j = 0

    sub_top = 0
    top = 0
    for j in range(i, k + 1):
        sub_top += nums[j]

    top = sub_top
    j += 1
    while j < len(nums):
        sub_top -= nums[i]
        sub_top += nums[j]

        top = max([top, sub_top])

        j += 1
        i += 1

    return top


nums = [1, 2, 3, 1, 4, 1, 1, 3]
print(max_sub_array(nums, 3))
