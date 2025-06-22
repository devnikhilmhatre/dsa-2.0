from dataclasses import dataclass


@dataclass
class MaxHeap:
    data: list

    def apply(self):
        top_index = 0
        top = self[top_index]

        for i in range(1, len(self.data)):
            if self.data[i] > top:
                top_index = i
                top = self.data[top_index]

        self.data[-1], self.data[top_index] = self.data[top_index], self.data[-1]
        