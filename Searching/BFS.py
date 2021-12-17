from collections import deque

def bfs(graph, start, visited):
    # use deque library to use queue
    queue = deque([start])
    # count the current note as visited
    visited[start] = True
    # repeat until the queue is empty
    while queue:
        # print one element from queue
        v = queue.popleft()
        print(v, end = ' ')
        # insert connected, unvisited nodes into the queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# call BFS
# example:
dfs(graph, 1, visited)
