def kruskal(sets, edges):
    """
    Create a minimum spanning tree

    :args:
        set: dict
        edges: list
    :return: dict
    """
    graph = {}

    for edge in edges:

        # if there is only one spanning tree left, break the loop
        if len(sets) == 1:
            break

        # find indexes of vertices
        set_one = find_set(edge[1])
        set_two = find_set(edge[2])

        # if vertices are not in same spanning tree, merge them
        if set_one != set_two:
            union(min(set_one, set_two), max(set_one, set_two), edge)

    return graph
