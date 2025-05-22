tests = [
    # capacity, values, weights
    (4, [1, 2, 3], [4, 5, 1], 3),
    (3, [1, 2, 3], [4, 5, 6], 0),
    (5, [10, 40, 30, 50], [5, 4, 2, 3], 80),
    (50, [60, 100, 120], [10, 20, 30], 220),
    (8, [15, 14, 10, 45, 30], [2, 5, 1, 3, 4], 85),
    (7, [60, 100, 120], [3, 4, 5], 160),
    (7, [10, 20, 30], [3, 3, 3], 50),
    (8, [20, 30, 50, 60], [1, 3, 4, 5], 100),
    (9, [70, 20, 50, 40], [5, 3, 4, 2], 120),
    # --- GPT Test Cases ---
    (9, [60, 20, 70, 10], [5, 3, 4, 1], 130),
    (6, [100, 20, 30, 60], [4, 3, 5, 2], 160),
    (7, [20, 50, 40, 100], [2, 3, 3, 4], 150),
    (5, [30, 60, 80, 10], [3, 2, 3, 1], 140),
    (10, [100, 60, 120], [6, 5, 4], 220),
    (8, [10, 50, 50, 40], [5, 3, 3, 2], 140),
    # Format: (capacity, values, weights, expected_max_value)
    # Case 1: Best combo is non-greedy (skip higher value early)
    # Pick: item 1 (value 70, wt 4), item 2 (value 30, wt 3) => total = 100
    # NOT: item 0 (value 90, wt 5) => total = 90
    (7, [90, 70, 30], [5, 4, 3], 100),
    # Case 2: Picking two smaller items beats one large
    # Pick: item 1 (60, 3) and item 2 (60, 2) = 120
    # NOT: item 0 (value 100, wt 5)
    (5, [100, 60, 60], [5, 3, 2], 120),
    # Case 3: Optimal is 3 items, greedy may pick just 2
    # Pick: items 1, 2, 3 (20+30+40=90, 1+2+2=5)
    # NOT: item 0 (value 80, wt 4)
    (5, [80, 20, 30, 40], [4, 1, 2, 2], 100),
    # Case 4: Equal weight but better total value from spread
    # Pick: item 1 (60, 3) + item 3 (60, 3) = 120
    # NOT: item 0 (100, 6)
    (6, [100, 60, 50, 60], [6, 3, 2, 3], 120),
    # Case 5: Greedy may pick 100 (wt=5), but 3 items are better
    # Pick: item 1 (40, wt=2), item 2 (50, wt=3), item 3 (30, wt=2) = 120
    (7, [100, 40, 50, 30], [5, 2, 3, 2], 140),
]

"""
(9, [70, 20, 50, 40], [5, 3, 4, 2])
With this test case answer should be 120, but we got 110.
Reason
we check 5+3 and then for next iteration skips 5, due to which we do not get expected output

### fixed this one by removing break statement, but introduced new bug

the main problem is the we are not check all the possible options and exit the process greedy way as soon as some match is found
without checking if there is another better match could be possible.
(50, [60, 100, 120], [10, 20, 30])

20, 30 case never get created as capacity 50 always get filled 

for 10, gets filled with 20
for 20, gets filled with 10
for 30, gets filled with 10

### sort weights and values in desc of values

test cases are working now

"""


def max_value(capacity, values, weights, ans):

    values, weights = zip(
        *sorted(zip(values, weights), key=lambda x: x[0], reverse=True)
    )

    maximum = 0
    for index_i in range(len(weights)):

        if weights[index_i] > capacity:
            continue
        sub_capacity = capacity - weights[index_i]
        sub_maximum = values[index_i]
        maximum = max([sub_maximum, maximum])
        if sub_capacity == 0:
            continue

        for index_j in range(len(weights)):
            if index_i == index_j:
                continue

            if weights[index_j] > sub_capacity:
                continue
            sub_capacity -= weights[index_j]
            sub_maximum += values[index_j]
            maximum = max([sub_maximum, maximum])

    return maximum, ans == maximum


class KnapSack:
    def __init__(self):
        self.mem = {}

    def max_value_2(
        self,
        capacity,
        values,
        weights,
        weight_index=0,
    ):

        key = (capacity, weight_index)

        if key in self.mem:
            return self.mem[key]

        if capacity <= 0 or weight_index >= len(weights):
            return 0
        if capacity < weights[weight_index]:
            self.mem[key] = self.max_value_2(
                capacity, values, weights, weight_index + 1
            )
            return self.mem[key]
        else:
            op1 = values[weight_index] + self.max_value_2(
                capacity - weights[weight_index],
                values,
                weights,
                weight_index + 1,
            )
            op2 = self.max_value_2(capacity, values, weights, weight_index + 1)
            self.mem[key] = max([op1, op2])
            return self.mem[key]

    def iterate(self, capacity, values, weights):
        mem = []
        for c in range(capacity + 1):
            mem.append([0 for _ in range(len(weights) + 1)])

        for cap in range(1, capacity + 1):
            for w in range(1, len(weights) + 1):
                if cap < weights[w - 1]:
                    mem[cap][w] = mem[cap][w - 1]
                else:
                    mem[cap][w] = max(
                        [
                            values[w - 1] + mem[cap - weights[w - 1]][w - 1],
                            mem[cap][w - 1],
                        ]
                    )
        return mem[-1][-1]


for data in tests:
    a, b, c, op = data
    ans = KnapSack().iterate(a, b, c)
    # if ans != op:
    print(data, ans == op, ans)
