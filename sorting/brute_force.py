def _min(data: list, ignore: set):
    minimum_index = None
    minimum = None

    for index, i in enumerate(data):
        if index in ignore:
            continue

        if minimum is None:
            minimum = i
            minimum_index = index

        if i < minimum:
            minimum = i
            minimum_index = index

    ignore.add(minimum_index)
    return minimum, ignore


def sort_brute_force(data: list):
    new_data = []
    ignore = set()
    for _ in range(len(data)):
        minimum, ignore = _min(data, ignore)
        new_data.append(minimum)

    return new_data


data = [4, 2, 6, 3, 2, 6, 3, 1, 0]

"""
index
[0, 1, 2, 3, 4, 5, 6, 7]

---
[2, 3, 6, 3, 2, 6, 3, 1]

---
[2, 3, 3, 6, 2, 6, 3, 1]

---
[2, 2, 3, 3, 6, 6, 3, 1]

---
[2, 2, 3, 3, 3, 6, 6, 1]

---
[1, 2, 2, 3, 3, 3, 6, 6,]

"""


def in_place_sort(data: list):
    index_1 = 0
    index_2 = 1

    while index_2 < len(data):
        if data[index_1] <= data[index_2]:
            index_1 += 1
            index_2 += 1
        else:
            data[index_1], data[index_2] = data[index_2], data[index_1]
            print(
                "swap", (data[index_1], data[index_2]), (data[index_2], data[index_1])
            )
            if index_1 > 0:
                index_1 -= 1
                index_2 -= 1

    return data


def merge_sorted_list(list_1: list, list_2: list):
    list_1_index = 0
    list_2_index = 0
    merged_list = []

    while list_1_index < len(list_1) and list_2_index < len(list_2):
        if list_1[list_1_index] <= list_2[list_2_index]:
            merged_list.append(list_1[list_1_index])
            list_1_index += 1
        else:
            merged_list.append(list_2[list_2_index])
            list_2_index += 1

    for i in range(list_1_index, len(list_1)):
        merged_list.append(list_1[i])

    for i in range(list_2_index, len(list_2)):
        merged_list.append(list_2[i])

    return merged_list


def merge(data: list, low: int, mid: int, high: int):
    new_data = []
    temp_low = low
    low_max = mid
    high_min = mid + 1

    while temp_low <= low_max and high_min <= high:
        if data[temp_low] <= data[high_min]:
            new_data.append(data[temp_low])
            temp_low += 1
        else:
            new_data.append(data[high_min])
            high_min += 1

    while temp_low <= low_max:
        new_data.append(data[temp_low])
        temp_low += 1

    while high_min <= high:
        new_data.append(data[high_min])
        high_min += 1

    for i in range(low, high + 1):
        data[i] = new_data[i - low]

    return data


def merge_sort(data: list, low: int, high: int):

    if low < high:
        # mid
        mid = (high + low) // 2

        # left, exclusive of mid
        merge_sort(data, low, mid)

        # right, inclusive of mid
        merge_sort(data, mid + 1, high)

        merge(data, low, mid, high)

    return data


def find_pivot(data: list, low: int, high: int):
    mid = (high + low) // 2

    low_value, mid_value, high_value = data[low], data[mid], data[high]

    if (low_value < mid_value < high_value) or (high_value < mid_value < low_value):
        return mid
    elif (mid_value < low_value < high_value) or (high_value < low_value < mid_value):
        return low
    else:
        return high


def shuffle(data: list, low: int, high: int):

    pivot = find_pivot(data, low, high)
    # print("shuffle", data, "|", "low", low, "high", high, "pivot", pivot)

    end = high
    data[end], data[pivot] = data[pivot], data[end]

    high -= 1
    while low <= high:
        if data[low] <= data[end]:
            low += 1
        elif data[high] > data[end]:
            high -= 1
        else:
            data[low], data[high] = data[high], data[low]

            low += 1
            high -= 1

    data[low], data[end] = data[end], data[low]

    # print("shuffle", data)
    return low


def quick_sort(data: list, low: int, high: int):
    # print("quick_sort", "low", low, "high", high)

    if low < high:
        pivot_point = shuffle(data, low, high)
        quick_sort(data, low, pivot_point - 1)
        quick_sort(data, pivot_point + 1, high)
    return data


print(quick_sort(data, 0, len(data) - 1))
