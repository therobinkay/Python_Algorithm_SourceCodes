INF = int(1e9)  # to denote infinity

# input number of nodes(n) and edges(m)
n = int(input())
m = int(input())
# make a 2-d list with all values set as INF
graph = [[INF] * (n+1) for _ in range(n+1)]
# cost pointed to self is set as 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # set C as a cost to go from A to B
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Run Floyd-Warshall algorithm
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print returned value
for a in range(1, n+1):
    for b in range(1, n+1):
        # print "INFINITY" if cannot be reached
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        # print the distance if can be reached
        else:
            print(graph[a][b], end=' ')
    print()
