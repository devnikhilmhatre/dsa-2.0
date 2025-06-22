from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


ten = root = TreeNode(10)
five = TreeNode(5)
one = TreeNode(1)
six = TreeNode(6)
fifteen = TreeNode(15)
twelve = TreeNode(12)

ten.left = five
ten.right = fifteen

five.left = one
five.right = six

fifteen.left = twelve

"""
      10
  5       15
1   6   -   12

"""

# root2 = fifteen
# fifteen.left = twelve
# twelve.left = ten
# ten.left = six
# six.left = five
# five.left = one


def pre_order_traversal(node: TreeNode):
    order = []

    def traversal(node: TreeNode):
        if node is None:
            return
        order.append(str(node.value))
        traversal(node.left)
        traversal(node.right)

    traversal(node)

    return " -> ".join(order)


# print(pre_order_traversal(root))


def insert(root: TreeNode, node: TreeNode):
    """
    considering we wont get duplicate key
    """
    if root is None:
        return node

    if node.value < root.value:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)

    return root


# root = insert(root, TreeNode(-1))
# root = insert(root, TreeNode(7))
# root = insert(root, TreeNode(4))
# print(pre_order_traversal(root))


def find(root: TreeNode, value: int):
    if root is None:
        return None

    if value == root.value:
        return root
    elif value < root.value:
        return find(root.left, value)
    else:
        return find(root.right, value)


# print(find(root, 0))


def find_min_max(node: TreeNode):
    if node is None:
        return None, None

    left_min, left_max = find_min_max(node.left)
    right_min, right_max = find_min_max(node.right)

    values = [
        i
        for i in [node.value, left_min, left_max, right_min, right_max]
        if i is not None
    ]

    return min(values), max(values)


def find_min(root: TreeNode):
    while root and root.left:
        root = root.left

    return root.value if root else None


def find_max(root: TreeNode):
    while root and root.right:
        root = root.right

    return root.value if root else None


def is_bst(node: TreeNode):
    if node is None:
        return True, None, None

    left_valid, left_min, left_max = is_bst(node.left)
    right_valid, right_min, right_max = is_bst(node.right)

    values = [
        i
        for i in [node.value, left_min, left_max, right_min, right_max]
        if i is not None
    ]

    is_valid = (
        (left_max is None or left_max < node.value)
        and (right_min is None or right_min > node.value)
        and left_valid
        and right_valid
    )
    return is_valid, min(values), max(values)


def lca(node: TreeNode, val_1: int, val_2: int):
    while node:
        if val_1 < node.value and val_2 < node.value:
            node = node.left
        elif val_1 > node.value and val_2 > node.value:
            node = node.right
        else:
            return node
    return node


@dataclass
class LinkNode:
    value: int
    next: Optional["LinkNode"] = None
    prev: Optional["LinkNode"] = None


def bst_doubly_linked_list(node: TreeNode):

    def traversal(node: TreeNode):
        if node is None:
            return

        yield from traversal(node.left)
        yield node.value
        yield from traversal(node.right)

    gen = traversal(node)

    def linked_list():
        head = None
        root = None
        for value in gen:
            print(value)
            node = LinkNode(value)
            if not root:
                root = head = node
                # head = head.next
                continue

            node.prev = head
            head.next = node

            head = head.next
        return root

    l = linked_list()
    print(l)


# bst_doubly_linked_list(root)

"""
Create BST from sorted array
"""


def sorted_list_to_bst(arr: list, low, high):
    if low > high:
        return None

    mid = (high + low) // 2

    node = TreeNode(arr[mid])

    node.left = sorted_list_to_bst(arr, low, mid - 1)
    node.right = sorted_list_to_bst(arr, mid + 1, high)
    return node


arr = list(range(1, 11))
sorted_tree_node = sorted_list_to_bst(arr, 0, len(arr) - 1)
print(pre_order_traversal(sorted_tree_node))
