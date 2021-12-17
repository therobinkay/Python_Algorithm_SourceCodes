def dfs(graph, v, visited):
    # count the current note as visited
    visited[v] = True
    print(v, end=' ')
    # visit the connected nodes to the current node recursively
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
# edges are shown as a 2-d list
# example:
graph = [
          [],
          [2, 3, 8],
          [1, 7],
          [1, 4, 5],
          [3, 5],
          [3, 4],
          [7],
          [2, 6, 8],
          [1, 7]
]

# represent the visited information as a 1-d list
# example:
visited = [False] * 9

# call DFS
# example:
dfs(graph, 1, visited)
