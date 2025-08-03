from dataclasses import dataclass
from typing import Optional


@dataclass
class Data:
    id: int


@dataclass
class DoubleNode:
    data: Data
    next: Optional["DoubleNode"] = None
    prev: Optional["DoubleNode"] = None


@dataclass
class Doubly:
    head: Optional[DoubleNode] = None
    tail: Optional[DoubleNode] = None

    def append(self, data):
        node = DoubleNode(data)

        if not self.tail:
            self.head = self.tail = node
            return

        tail = self.tail
        tail.next = node
        node.prev = tail
        self.tail = node

    def prepend(self, data):
        node = DoubleNode(data)

        if not self.head:
            self.head = self.tail = node
            return

        head = self.head
        head.prev = node
        node.next = head
        self.head = node

    def delete(self, id):
        node = self.find(id)
        if not node:
            return

        prev = node.prev
        next = node.next

        if prev:
            prev.next = next
        else:
            self.head = next

        if next:
            next.prev = prev
        else:
            self.tail = prev

    def find(self, id):
        head = self.head

        while head:
            if head.data.id == id:
                return head
            head = head.next

        return None

    def delete_head(self):
        head = self.head
        if not head:
            return
        head = head.next
        if head:
            head.prev = None
        self.head = head

    def delete_tail(self):
        tail = self.tail
        if not tail:
            return
        tail = tail.prev
        if tail:
            tail.next = None
        self.tail = tail

    def reverse(self):
        head = self.head
        if not head:
            return

        while head:
            prev = head.prev
            next = head.next

            head.prev = next
            head.next = prev

            head = next

        self.head, self.tail = self.tail, self.head
