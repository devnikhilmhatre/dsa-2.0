from linked_list import get_singly, get_cyclic_singly
from linked_list.node import Data

if __name__ == "__main__":
    singly = get_cyclic_singly(end=10)
    # singly.represent()
    print(singly.is_cyclic())
    # singly.in_place_reverse()
    # singly.delete(Data(3))
    # singly.delete(Data(1))
    # singly.in_place_reverse()
    # singly.represent()
    # singly.insert_at(Data(1), 6)
    # singly.represent()

    # singly_2 = get_singly(9)

    # singly.merge(singly_2.head)
    # singly.represent()
