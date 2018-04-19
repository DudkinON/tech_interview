from algorithms.binary_search_tree import BST


def question4(m, r, n1, n2):

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
