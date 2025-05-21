# from linked_list import get_singly, get_cyclic_singly
# from linked_list.node import Data

# from binary_tree.node import root, height

# if __name__ == "__main__":
#     pass
# height(root)
# singly = get_cyclic_singly(end=10)
# singly.represent()
# print(singly.is_cyclic())
# singly.in_place_reverse()
# singly.delete(Data(3))
# singly.delete(Data(1))
# singly.in_place_reverse()
# singly.represent()
# singly.insert_at(Data(1), 6)
# singly.represent()

# singly_2 = get_singly(9)

# singly.merge(singly_2.head)
# singly.represent()


class Data:
    def __init__(self):
        self.collection = []
        self.memory = {}

    def recurse(self, str1, str2, depth=0):
        # self.collection.append([str1, str2, depth])
        # print(str1, str2, depth)
        if len(str1) <= 0 or len(str2) <= 0:
            return 0

        if str1[0] == str2[0]:
            return 1 + self.recurse(str1[1:], str2[1:], depth + 1)
        else:
            return max(
                [
                    self.recurse(str1[1:], str2, depth + 1),
                    self.recurse(str1, str2[1:], depth + 1),
                ]
            )

    def iterate(self, str1, str2, depth=0):

        memory = []
        for i in range(len(str1)):
            m = []
            for j in range(len(str2)):
                m.append(0)
            memory.append(m)

        for index_1 in range(len(str1)):
            for index_2 in range(len(str2)):
                key = (index_1, index_2)
                self.memory.setdefault(key, 0)
                print(f"{index_1}:{str1[index_1]}", f"{index_2}:{str2[index_2]}")
                if str1[index_1] == str2[index_2]:
                    self.memory[key] = (
                        1
                        + self.memory.get((index_1 - 1, index_2 - 1), 0)
                        # + self.memory.get(key, 0)
                    )

                else:
                    self.memory[key] = max(
                        [
                            self.memory.get((index_1 - 1, index_2), 0),
                            self.memory.get((index_1, index_2 - 1), 0),
                        ]
                    )
                memory[index_1][index_2] = self.memory[key]

        for m in memory:
            print(m)
        return memory[index_1][index_2]


str1 = "abcde"
str2 = "ace"
d = Data()
print(d.iterate(str1, str2, 0))

"""
Construct lcs string
"""


# groups = {}

# for i in d.collection:
#     groups.setdefault(i[2], [])
#     groups[i[2]].append(i)
#     i.pop()


# for depth, groups in groups.items():
#     print(depth, groups)
