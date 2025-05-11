from linked_list.singly import Singly
from linked_list.node import Data


def get_singly(end=6):
    data = (Data(i) for i in range(1, end))

    singly = Singly()
    for item in data:
        singly.append(item)

    return singly
