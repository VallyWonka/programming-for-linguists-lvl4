def dijkstra(graph, vertex):
    visited = []

    node_distances = {node: float("inf") for node in graph.keys()}
    node_distances[vertex] = 0

    while True:
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                new_distance = node_distances[vertex] + graph[vertex][neighbour]
                if new_distance < node_distances[neighbour]:
                    node_distances[neighbour] = new_distance
        visited.append(vertex)
        if len(visited) == len(graph.keys()):
            break
        vertex = min({node: distance for node, distance in node_distances.items() if node not in visited}.items(),
                     key=lambda x: x[1])[0]
    return node_distances, visited
