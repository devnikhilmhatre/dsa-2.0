from dataclasses import dataclass
from typing import Optional
from linked_list.node import SingleNode

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

    def append(self, data: dict):
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

    def represent(self):
        head = self.head
        while head:
            print(head.data.id, "> ", end="")
            head = head.next
        print("End")

    def reverse(self):
        current = self.head
        previous = None

        while current:
            upcoming = current.next  # access the current, so it has became previous now
            current.next = previous  # since next is accessed, it can be replaced
            previous = current

            current = upcoming  # move pointer next one
        self.head = previous

    def insert_at_head(self, data: dict):
        node = SingleNode(data=data)
        node.next = self.head
        self.head = node

    def delete(self, data: dict):
        node = SingleNode(data)
        current = self.head
        previous = None

        while current.next:
            if current.data.id == node.data.id:
                previous.next = current.next
            previous = current
            current = current.next
