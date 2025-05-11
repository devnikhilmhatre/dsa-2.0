from dataclasses import dataclass
from linked_list.node import DoubleNode
from typing import Optional


@dataclass
class Doubly:
    head: Optional["DoubleNode"] = None

    def append(self, data: dict):
        node = DoubleNode(data=data)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node
        node.prev = current
