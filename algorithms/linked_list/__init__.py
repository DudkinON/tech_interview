class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class List(object):
    def __init__(self, r):
        self.root = Node(r)
        self.end = self.root
        self.current = self.root
        self.length = 1

    def insert(self, number):
        self.end.next = Node(number)
        self.end = self.end.next
        self.length += 1
