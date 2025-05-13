from linked_list.singly import Singly
from linked_list.node import Data


def get_singly(end=6):
    data = (Data(i) for i in range(1, end))

    singly = Singly()
    for item in data:
        singly.append_data(item)

    return singly


def get_cyclic_singly(end=6):
    data = (Data(i) for i in range(1, end))

    singly = Singly()
    for item in data:
        if item.id == end - 1:
            middle = singly.find_middle_count()
            node = singly.get_node(item)
            node.next = middle
            singly.append_node(node)
        else:
            singly.append_data(item)

    return singly
