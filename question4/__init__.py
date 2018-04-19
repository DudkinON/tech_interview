from algorithms.binary_search_tree import BST


def question4(m, r, n1, n2):
    def read_matrix(m):
        binary_tree = None
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 1:
                    if binary_tree is None:
                        binary_tree = BST(i)
                        binary_tree.insert(j)
                    else:
                        if j == binary_tree.root.value:
                            temp_tree = binary_tree
                            binary_tree = BST(i)
                            binary_tree.insert(j)
                            binary_tree.add(temp_tree)
                        else:
                            if binary_tree.root.value == i:
                                binary_tree.insert(j)
        return binary_tree

    tree = read_matrix(m)
    assert tree.root.value == r
    return tree.search_parent(n1, n2)


def main():
    matrix = [[0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]]
    print question4(matrix, 3, 1, 4)


if __name__ == '__main__':
    main()
