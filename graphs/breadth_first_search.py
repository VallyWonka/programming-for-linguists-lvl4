visited = []


def bfs(graph, start):
    global visited
    visited.extend(start)
    print(f"visited {visited}")

    new_wave = [child_edge for edge in start for child_edge in graph[edge] if child_edge not in visited]
    if new_wave:
        print(f"new wave {new_wave}")
        bfs(graph, new_wave)
