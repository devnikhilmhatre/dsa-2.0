from linked_list.node import Data
from linked_list.algorithms import get_singly


def reverse():
    singly = get_singly()
    singly.represent()
    singly.delete(Data(2))
    singly.represent()
    singly.reverse()
    singly.represent()
