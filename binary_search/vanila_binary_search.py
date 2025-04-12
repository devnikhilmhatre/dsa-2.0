def binary_search(data, search, low, high):

    if not data:
        return -1

    """
    for index, element in enumerate(data):
        if element == search:
            return index
    """
    while low <= high:
        mid = (low + high) // 2

        if data[mid] == search:
            return mid
        elif data[mid] > search:
            low = mid + 1
        else:
            high = mid - 1

    return -1


"""
1. data is empty; return -1
2. search is not present in data; return -1
3. data is not sorted; not possible to check, we'll run out of execution time
"""

tests = [
    {"data": list(range(10, 0, -1)), "search": 6, "result": 4},
    {
        "data": sorted(list(range(10, 0, -1)) + list(range(10, 0, -1)), reverse=True),
        "search": 6,
        "result": 9,
    },
    {"data": list(range(1000000, 0, -1)), "search": 999999, "result": 1},
    {"data": list(), "search": 99999, "result": -1},
    {"data": list(range(10, 0, -2)), "search": 5, "result": -1},
    {"data": list(range(10, -5, -1)), "search": -2, "result": 12},
]


for index, test in enumerate(tests):
    result = binary_search(test["data"], test["search"], 0, len(test["data"]) - 1)
    print(f"Index: {index}", f"Result: {result}", result == test["result"])
