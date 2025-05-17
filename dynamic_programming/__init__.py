def longest_common_sequence(list_1: list, list_2: list):
    map_1 = {}
    map_2 = {}
    for index, i in enumerate(list_1):
        map_1.setdefault(i, [])
        map_1[i].append(index)

    for index, i in enumerate(list_2):
        map_2.setdefault(i, [])
        map_2[i].append(index)

    common = set(map_1.keys()).intersection(set(map_2.keys()))
    if len(common) < 2:
        return len(common)

    map_1_copy = dict(map_1)

    def sort_key(value):
        return list(map_1_copy[value]).pop(0)

    common = sorted(common, key=sort_key)
    count = 1
    max_count = []
    pointer_1, pointer_2 = 0, 1
    while pointer_2 < len(common):
        if pointer_1 == 2 and pointer_2 == 3:
            pass
        char_1 = common[pointer_1]
        char_2 = common[pointer_2]
        map_1_pointer_1 = map_1[char_1].pop(0)
        map_1_pointer_2 = map_1[char_2].pop(0)
        map_2_pointer_1 = map_2[char_1].pop(0)
        map_2_pointer_2 = map_2[char_2].pop(0)

        if map_1_pointer_2 > map_1_pointer_1 and map_2_pointer_2 > map_2_pointer_1:
            count += 1
        else:
            max_count.append(count)
            count = 1
        # map_1[char_2].insert(0, map_1_pointer_2)
        # map_2[char_2].insert(0, map_2_pointer_2)
        pointer_1 += 1
        pointer_2 += 1

    max_count.append(count)

    return max(max_count)


print(longest_common_sequence([i for i in "abcdea"], [i for i in "adbefcdpea"]))

"""
"abcde"
"ace" 
"""
