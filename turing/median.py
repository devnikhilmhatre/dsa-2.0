def min_operations_to_median_k(nums: list, k: int):
    nums.sort()
    median_index = len(nums) // 2
    return abs(nums[median_index] - k)


nums = [3, 7, 1, 4, 6]
k = 1
ans = min_operations_to_median_k(nums, k)
print(ans == 8, ans)
