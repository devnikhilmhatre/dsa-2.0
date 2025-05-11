from linked_list.algorithms import get_singly


def find_middle_count():
    singly = get_singly(11)

    count = 0
    current = singly.head

    while current:
        count += 1
        current = current.next

    mid = count // 2

    current = singly.head
    count = 0
    while current:
        if count == mid:
            print(f"mid: {mid}", f"current: {current}")
            return
        count += 1
        current = current.next


def find_middle_fast_slow():
    singly = get_singly(11)

    slow_pointer = singly.head
    fast_pointer = singly.head.next

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    print(f"mid: {slow_pointer.next}")
