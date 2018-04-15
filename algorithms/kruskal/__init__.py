def kruskal(sets, edges):
    """
    Create a minimum spanning tree

    :args:
        set: dict
        edges: list
    :return: dict
    """
    graph = {}

    def find_set(key):
        """
        Find key in sets and return index

        :param key: str
        :return: int
        """
        for i in xrange(len(sets)):
            if key in sets[i]:
                return i
        return -1

    def union(less, more, edge):
        """
        Union of two sets by indexes, in set with min index,
        then remove set with max index. Then append the edge
        in _edges which contains edges for a minimum spanning
        tree.

        :args:
            less: A min int
            more: A max int
            edge:
                A list like [5, 'B', 'C'] where 5 is a value
                of edge 'B', and 'C' are vertices
        :return: void
        """

        sets[less] = set.union(sets[less], sets[more])
        sets.pop(more)
        add_edge(edge[1], (edge[2], edge[0]))
        add_edge(edge[2], (edge[1], edge[0]))

    def add_edge(key, body):

        if key in graph:
            graph[key].append(body)
        else:
            graph[key] = [body]

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
