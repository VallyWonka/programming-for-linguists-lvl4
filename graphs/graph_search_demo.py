from graphs import dfs, bfs


graph = {'A': ['F', 'B'],
         'B': ['A', 'C', 'E'],
         'C': ['B', 'D'],
         'D': ['C'],
         'E': ['B'],
         'F': ['G', 'A'],
         'G': ['F']}

print("Depth-First Search")
dfs(graph, 'A')

print()

print("Breadth-First Search")
bfs(graph, ['A'])
