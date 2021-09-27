visited = []


def dfs(graph, start):
    global visited

    if start not in visited:
        visited.append(start)
        print(f"visited {start}")

    edges = graph.get(start, [])
    print(f"edges from visited {edges}")

    for edge in edges:
        if edge not in visited:
            print(f"going to {edge}")
            return dfs(graph, edge)
    else:
        for edge in graph.keys():
            if edge not in visited:
                return dfs(graph, edge)
