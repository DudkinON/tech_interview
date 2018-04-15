from algorithms.kruskal import kruskal


def question3(G):

    # create edges
    edges = []

    # create edges
    for i in G:
        for j in G[i]:
            item = sorted([i, j[0], j[1]])
            if item not in edges:
                edges.append(item)

    return kruskal([set(i) for i in G], sorted(edges))
