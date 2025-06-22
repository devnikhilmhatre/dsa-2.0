def next_largest(arr: list):
    data = [-1]

    j = len(arr) - 1
    i = j - 1
    while i >= 0:
        largest = -1
        temp_j = j
        while j > i:
            print(i, j, "|", arr[i], arr[j])
            if arr[j] > arr[i]:
                largest = arr[j]
                temp_j = j
            j -= 1

        data.append(largest)
        j = temp_j
        i -= 1

    return data[::-1]


def next_largest_stack(arr: list):
    data = []
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        i = arr[i]
        while stack and stack[-1] < i:
            stack.pop()

        if stack:
            data.append(stack[-1])
        else:
            data.append(-1)

        stack.append(i)

    return data[::-1], len(data)


def next_smallest_stack(arr: list):
    data = []
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        i = arr[i]
        while stack and stack[-1] > i:
            stack.pop()

        if stack:
            data.append(stack[-1])
        else:
            data.append(-1)

        stack.append(i)

    return data[::-1], len(data)


def prev_largest_stack(arr: list):
    data = []
    stack = []

    for i in arr:
        while stack and stack[-1] < i:
            stack.pop()

        if stack:
            data.append(stack[-1])
        else:
            data.append(-1)

        stack.append(i)

    return data, len(data)


def prev_smallest_stack(arr: list):
    data = []
    stack = []

    for i in arr:
        while stack and stack[-1] > i:
            stack.pop()

        if stack:
            data.append(stack[-1])
        else:
            data.append(-1)

        stack.append(i)

    return data, len(data)


# arr = [1, 8, 6, 4, 5, 3, 7]
# print(arr, len(arr))
# print(*prev_smallest_stack(arr))


def rain_water(arr: list):
    i = 0
    j = i + 1

    total = 0

    while i < len(arr):
        mid_heights = []
        last_height_index = i
        last_height = arr[last_height_index]
        while j < len(arr):
            if arr[j] >= last_height:
                collected = min([last_height, arr[j]])

                gaps = (j - last_height_index) - 1
                print(collected, "|", gaps)
                last_height = arr[j]
                last_height_index = j

                if gaps <= 0:
                    j += 1
                    continue

                collected = collected * gaps
                if mid_heights:
                    for mid_height in mid_heights:
                        collected -= mid_height
                    mid_heights = []

                total += collected
                break
            mid_heights.append(arr[j])
            j += 1

        i = last_height_index + (1 if mid_heights else 0)
        j = i + 1

    return total


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("rain_water: ", rain_water(arr))
