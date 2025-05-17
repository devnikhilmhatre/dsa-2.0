def polynomial_multiplication(list_1: list, list_2: list):
    result = {}
    for index_i, i in enumerate(list_1):
        for index_j, j in enumerate(list_2):
            if 0 in (i, j):
                continue
            key = index_i + index_j
            result.setdefault(key, [])
            result[key].append(i * j)

    return [sum(result[key]) for key in sorted(result.keys())]


print(polynomial_multiplication([2, 0, 5, 7], [3, 4, 2]))
