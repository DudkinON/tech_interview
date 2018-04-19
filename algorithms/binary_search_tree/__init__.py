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
        """
        Insert an integer to binary tree

        :param new_val: An integer
        :return: void
        """
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        """
            Using recursion detect place for an integer in binary tree and
            insert it

        :param current: An object of class Node
        :param new_val: An integer
        :return: void
        """
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
        """
        Merge binary tree with the current binary tree

        :param node: An object of Node class
        :return: void
        """
        if self.root.value < node.root.value:
            self.root.right = node.root
        else:
            self.root.left = node.root

    def search(self, find_val):
        """
        Search the integer in binary tree

        :param find_val: An integer
        :return: result of search_helper method
        """
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        """
        Using recursion search an integer in binary tree

        :param current: An object of Node class
        :param find_val: An integer
        :return: Boolean
        """
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

    def search_parent_helper(self, n1, n2, node):
        if node:
            if node.value == n1 or node.value == n2:
                return node.value

            if node.left is not None and node.right is not None:
                if (self.search_helper(node.left, n1) and
                        self.search_helper(node.right, n2) or
                        self.search_helper(node.left, n2) and
                        self.search_helper(node.right, n1)):
                    return node.value
                elif self.search_helper(node.left, n1):
                    return self.search_parent_helper(n1, n2, node.left)
                else:
                    return self.search_parent_helper(n1, n2, node.right)
            elif node.left is None:
                return self.search_parent_helper(n1, n2, node.right)
            elif node.right is None:
                return self.search_parent_helper(n1, n2, node.left)

    def search_parent(self, n1, n2):
        return self.search_parent_helper(n1, n2, self.root)
