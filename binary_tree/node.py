from dataclasses import dataclass
from typing import Optional

"""
    1
  2   3
4   5
"""


@dataclass
class TreeNode:
    value: int = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


one = root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)


one.left = two
one.right = three
two.left = four
two.right = five
# four.left = six


def pre_order_travel(node: TreeNode):
    if node is None:
        return
    print(node.value, end=" ")
    pre_order_travel(node.left)
    pre_order_travel(node.right)


def in_order_travel(node: TreeNode):
    if node is None:
        return
    in_order_travel(node.left)
    print(node.value, end=" ")
    in_order_travel(node.right)


def post_order_travel(node: TreeNode):
    if node is None:
        return
    post_order_travel(node.left)
    post_order_travel(node.right)
    print(node.value, end=" ")


def height(node: TreeNode):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


class Balanced:
    def __init__(self):
        self.balanced = True

    def is_balanced(self, node: TreeNode):
        if node is None:
            return 0
        left_height = self.is_balanced(node.left)
        if not self.balanced:
            return 0
        right_height = self.is_balanced(node.right)
        if not self.balanced:
            return 0
        if abs(right_height - left_height) > 1:
            self.balanced = False
        return 1 + max(left_height, right_height)


def search(node: TreeNode, value):
    if node is None:
        return False

    if node.value == value:
        return True
    left_check = search(node.left, value)
    if left_check:
        return True

    right_check = search(node.right, value)
    if right_check:
        return True

    return False


class Total:
    def __init__(self):
        self.total = 0

    def count(self, node: TreeNode):
        if node is None:
            return 0

        self.total += 1

        self.count(node.left)
        self.count(node.right)


class LeafNodes:
    def __init__(self):
        self.leaf = 0

    def count_leaf_nodes(self, node: TreeNode):
        if node is None:
            return
        left = self.count_leaf_nodes(node.left)
        right = self.count_leaf_nodes(node.right)
        if left is None and right is None:
            self.leaf += 1


def internal_nodes(node: TreeNode):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 0
    return 1 + internal_nodes(node.left) + internal_nodes(node.right)


def one_child(node: TreeNode):
    pass


def sum(node: TreeNode):
    if node is None:
        return 0
    return node.value + sum(node.left) + sum(node.right)


def max_value(node: TreeNode):
    if node is None:
        return 0
    left = max_value(node.left)
    right = max_value(node.right)

    return max(left, right, node.value)


def invert(node: TreeNode):
    if node is None:
        return node

    left = invert(node.left)
    right = invert(node.right)

    node.right = left
    node.left = right

    return node


# pre_order_travel(root)
# print()
# inverted_node = invert(root)
# print()
# pre_order_travel(inverted_node)
