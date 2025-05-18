def longest_common_sequence_custom(list_1: list, list_2: list):
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


# print(longest_common_sequence_custom([i for i in "abcdeaf"], [i for i in "adbdeafcpea"]))


class Solution:

    def lcs2(self, text1, text2):
        for index1, i in enumerate(text1):
            index1 += 1
            for index2, j in enumerate(text2):
                index2 += 1
                if i == j:
                    self.values[(index1, index2)] = 1 + max(
                        [self.values.get((index1 - 1, index2 - 1), 0), 0]
                    )
                else:
                    self.values[(index1, index2)] = max(
                        [
                            self.values.get((index1 - 1, index2), 0),
                            self.values.get((index1, index2 - 1), 0),
                        ]
                    )
        return self.values[len(text1), len(text2)]

    def lcs(self, text1, text2, i, j):
        print(text1[: i + 1], text2[: j + 1], "-" * 5)
        if i >= len(text1) or j >= len(text2):
            return 0

        if (i, j) in self.values:
            return self.values.get((i, j))

        if text1[i] == text2[j]:
            self.values[(i, j)] = 1 + self.lcs(text1, text2, i + 1, j + 1)
        else:
            v1 = self.lcs(text1, text2, i + 1, j)
            v2 = self.lcs(text1, text2, i, j + 1)
            self.values[(i, j)] = max(v1, v2)

        print(text1[: i + 1], text2[: j + 1], self.values[(i, j)])
        return self.values[(i, j)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.values = {}
        return self.lcs2(text1, text2)


text1 = "ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
text2 = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

from datetime import datetime

start = datetime.now()
text1 = "bsbininm"
text2 = "jmjkbkjkv"
print(Solution().longestCommonSubsequence(text1, text2))
print(datetime.now() - start)
