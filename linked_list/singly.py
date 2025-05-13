from dataclasses import dataclass
from typing import Optional
from linked_list.node import SingleNode, Data

"""
singly
    head
        data, next
                data, next
                        data, next
                                data, next
"""


@dataclass
class Singly:
    head: Optional[SingleNode] = None

    def get_node(self, data):
        return SingleNode(data=data)

    def append_data(self, data: dict):
        # create node
        node = SingleNode(data=data)

        # attach head if not preset
        if not self.head:
            self.head = node
            return

        # find tail (node with next value set to None)
        # attach new node to tail.next
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node

    def append_node(self, node: SingleNode):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node

    def represent(self):
        head = self.head
        while head:
            print(head.data.id, "> ", end="")
            head = head.next
        print("End")

    def insert_at_head(self, data: dict):
        node = SingleNode(data=data)
        node.next = self.head
        self.head = node

    def delete(self, data: dict):
        node = SingleNode(data)
        current = self.head
        previous = None

        while current:
            if current.data.id == node.data.id:
                previous.next = current.next
            previous = current
            current = current.next

    def find_middle_count(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        mid = count // 2

        current = self.head
        count = 0
        while current:
            if count == mid:
                print(f"mid: {mid}", f"current: {current}")
                return current
            count += 1
            current = current.next

    def find_middle_fast_slow(self):

        slow_pointer = self.head
        fast_pointer = self.head.next

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        print(f"mid: {slow_pointer.next}")

    def in_place_reverse(self):
        current = self.head
        previous = None

        while current:
            upcoming = current.next

            current.next = previous
            previous = current

            current = upcoming

        self.head = previous

    def insert_at(self, data, index):
        if index == 0:
            self.insert_at_head(data=data)
            return
        node = SingleNode(data=data)

        count = 0
        current = self.head
        previous = None

        while current:
            count += 1
            previous = current
            current = current.next
            if count == index:
                previous.next = node
                node.next = current

    def merge(self, current_2: SingleNode):
        current_1 = self.head
        node = SingleNode(data=Data(-1))
        new = node

        while current_1 and current_2:
            if current_2.data.id < current_1.data.id:
                new.next = current_2
                current_2 = current_2.next
            else:  # current_2.data.id >= current_1.data.id
                new.next = current_1
                current_1 = current_1.next
            new = new.next

        if current_1:
            new.next = current_1
        elif current_2:
            new.next = current_2

        self.head = node.next

    def is_cyclic(self):
        print("is_cyclic:start")
        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            if slow.data.id == fast.data.id:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
