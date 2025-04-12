"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def desc_binary_search_or_insert_index(data, search, low, high):

    if not data:
        return low

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == search:
            return mid
        elif data[mid] > search:
            low = mid + 1
        else:
            high = mid - 1

    return low


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
    {"data": list(), "search": 99999, "result": 0},
    {"data": list(range(10, 0, -2)), "search": 5, "result": 3},
    {"data": list(range(10, -5, -1)), "search": -2, "result": 12},
]


for index, test in enumerate(tests):
    result = binary_search(test["data"], test["search"], 0, len(test["data"]) - 1)
    print(f"Index: {index}", f"Result: {result}", result == test["result"])
