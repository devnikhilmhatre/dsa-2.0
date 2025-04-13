"""
Unable to solve it 13th April 2025
"""

# """
# Given an integer array num sorted in non-decreasing order.

# You can perform the following operation any number of times:

# Choose two indices, i and j, where nums[i] < nums[j].
# Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.
# """

# tests = [
#     {"nums": [1, 2, 3, 4], "result": 0},
#     {"nums": [1, 1, 2, 2, 3, 3], "result": 0},
#     {"nums": [1000000000, 1000000000], "result": 2},
#     {"nums": [2, 3, 4, 4, 4], "result": 1},
#     {"nums": [2], "result": 1},
# ]


# def array_len_after_removal_of_pairs(nums: list):

#     if len(nums) < 2:
#         return len(nums)

#     length = len(nums)

#     for i_index, i in enumerate(nums):
#         if i == -1:
#             continue
#         for j_index, j in enumerate(nums):
#             if j == -1:
#                 continue

#             if i < j:
#                 nums[i_index] = -1
#                 nums[j_index] = -1
#                 length -= 2

#     return 0 if length < 0 else length


# for index, test in enumerate(tests):
#     result = array_len_after_removal_of_pairs(test["nums"])
#     print(f"Index: {index}", f"Result: {result}", result == test["result"])
