class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        self.current_parent = self.root

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
