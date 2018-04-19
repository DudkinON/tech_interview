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

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def add(self, node):
        if self.root.value < node.root.value:
            self.root.right = node.root
        else:
            self.root.left = node.root

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

    def pre_order(self, node, target):
        if node:
            if node.value == target:
                return True
            else:
                return (self.pre_order(node.left, target) or
                        self.pre_order(node.right, target))
        return False

    def search_parent_helper(self, n1, n2, node):
        if node:
            if node.value == n1 or node.value == n2:
                return node.value

            if node.left is not None and node.right is not None:
                if (self.pre_order(node.left, n1) and
                        self.pre_order(node.right, n2) or
                        self.pre_order(node.left, n2) and
                        self.pre_order(node.right, n1)):
                    return node.value
                elif self.pre_order(node.left, n1):
                    return self.search_parent_helper(n1, n2, node.left)
                else:
                    return self.search_parent_helper(n1, n2, node.right)
            elif node.left is None:
                return self.search_parent_helper(n1, n2, node.right)
            elif node.right is None:
                return self.search_parent_helper(n1, n2, node.left)
