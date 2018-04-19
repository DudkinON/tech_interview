from algorithms.linked_list import List


def question5(ll, m):
    if not isinstance(ll, List):
        return None
    if type(m) != int:
        return None
    for i in range(ll.length - m):
        ll.next()
    return ll.current.data


if __name__ == '__main__':
    linked_list = List(2)
    linked_list.insert(4)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(9)
    linked_list.insert(0)
    print 6 == question5(linked_list, 3)

