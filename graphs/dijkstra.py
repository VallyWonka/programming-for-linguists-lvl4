graph = {'A': {'D':8, 'B':5, 'F':2},
         'B': {'A':5, 'C':4, 'E':13},
         'C': {'B':4, 'D':6},
         'D': {'C':6, 'A':8, 'F':10, 'E':4},
         'E': {'D':4, 'B':13, 'F':3},
         'F': {'E':3, 'A':2, 'D':10}}


def dijkstra(vertex, graph):
    visited = []

    node_distances = {node: float("inf") for node in graph.keys()}
    node_distances[vertex] = 0

    if len(visited) == len(graph.keys()):
        return


dijkstra("A", graph)
