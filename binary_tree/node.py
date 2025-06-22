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
three.right = six


def pre_order_travel(node: TreeNode, arr: list):
    if node is None:
        return
    arr.append(node.value)
    pre_order_travel(node.left, arr)
    pre_order_travel(node.right, arr)


def in_order_travel(node: TreeNode, arr: list):
    if node is None:
        return
    in_order_travel(node.left, arr)
    arr.append(node.value)
    in_order_travel(node.right, arr)


def post_order_travel(node: TreeNode, arr: list):
    if node is None:
        return
    post_order_travel(node.left, arr)
    post_order_travel(node.right, arr)
    # print(node.value, end=" ")
    arr.append(node.value)


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
# in_order_travel(root)
# print()
# post_order_travel(root)
# print()
# print()
# inverted_node = invert(root)
# print()
# pre_order_travel(inverted_node)


def sorted_list_to_bst(arr: list, low, high):
    if low > high:
        return None

    mid = (high + low) // 2

    node = TreeNode(arr[mid])

    node.left = sorted_list_to_bst(arr, low, mid - 1)
    node.right = sorted_list_to_bst(arr, mid + 1, high)
    return node


def main():

    arr = list(range(1, 11))
    sorted_tree_node = sorted_list_to_bst(arr, 0, len(arr) - 1)
    # print(sorted_tree_node)
    in_order_travel(sorted_tree_node)
    print()


def recreate_graph(pre_order_list: list, in_order_travel_list, in_order_dict: dict):
    """
    #### This will only work with unique node/array values
    use in order list index to while traversing
    index will let us know when we reach end (< 0 or > length of list)
    the end will tell to switch the other side of tree (from left -> right || from right -> left)
    """

    pre_order_list_index = 0

    def helper(low, high):
        nonlocal pre_order_list_index
        in_order_travel_list

        if low > high:
            return None

        # pick start of unvisited index
        node = TreeNode(pre_order_list[pre_order_list_index])
        node_index = in_order_dict.get(pre_order_list[pre_order_list_index])
        pre_order_list_index += 1

        node.left = helper(low, node_index - 1)
        node.right = helper(node_index + 1, high)

        return node

    return helper


def print_tree_horizontal(node: TreeNode, prefix="", is_left=True):
    if node is not None:
        print_tree_horizontal(
            node.right, prefix + ("│   " if is_left else "    "), False
        )
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        print_tree_horizontal(node.left, prefix + ("    " if is_left else "│   "), True)


def find(node: TreeNode, key, parent=None, direction=None):
    if not node:
        return (None, parent, direction)
    if node.value == key:
        return (node, parent, direction)
    elif node.value > key:
        return find(node.left, key, node, "left")
    else:
        return find(node.right, key, node, "right")


def delete_node_from_bst():
    five = root = TreeNode(5)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    six = TreeNode(6)
    seven = TreeNode(7)

    five.left = three
    five.right = six

    three.left = two
    three.right = four

    six.right = seven

    print_tree_horizontal(root)

    delete = 3

    node_to_be_deleted, parent, direction = find(root, delete)
    # print(node_to_be_deleted)

    in_order_travel_list = []
    pre_order_travel_list = []
    in_order_travel(node_to_be_deleted, in_order_travel_list)
    pre_order_travel(node_to_be_deleted, pre_order_travel_list)

    pre_order_travel_list = [i for i in pre_order_travel_list if i != delete]
    in_order_travel_list = [i for i in in_order_travel_list if i != delete]

    helper = recreate_graph(
        pre_order_travel_list,
        in_order_travel_list,
        {value: index for index, value in enumerate(in_order_travel_list)},
    )

    new_node = helper(0, len(in_order_travel_list) - 1)
    print("-" * 25)
    if direction == "left":
        parent.left = new_node
    else:
        parent.right = new_node

    print_tree_horizontal(root)
    return root


delete_node_from_bst()
