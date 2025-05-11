from linked_list.singly import Singly
from linked_list.node import Data

data = (Data(i) for i in range(1, 6))


def reverse():
    singly = Singly()
    for item in data:
        singly.append(item)

    singly.represent()
    singly.delete(Data(2))
    singly.represent()
    singly.reverse()
    singly.represent()
