mid = 2
data = list(range(mid, 5))
data += list(range(-2, mid))


def rotated_at(nums: list):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2

        if mid and nums[mid] < nums[mid - 1]:
            return mid, nums[mid - 1]
        elif nums[mid] < nums[0]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, 0


print(data)
print(rotated_at(data))
