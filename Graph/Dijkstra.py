import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # to denote infinity

# input number of nodes(n) and edges(m)
n, m = map(int, input().split())
# input the starting node number
start = int(input())
# create a list that holds the connectivity information
graph = [[] for i in range(n + 1)]
# set all values of the shortest path table to INF
distance = [INF] * (n + 1)

# input all edge information
for _ in range(m):
    a, b, c = map(int, input().split())
    # set C as a cost to go from A to B
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    # set 0 as the cost to the starting node and insert it into the queue
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # while the queue is not empty
        # get the info of the node with the shortest distance
        dist, now = heapq.heappop(q)
        # if the current node is already processed, ignore
        if distance[now] < dist:
            continue
        # examine connected nodes to the current node
        for i in graph[now]:
            cost = dist + i[1]
            # update if the distance that goes through the current node is shorter
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            

# run Dijkstra Shortest Path algorithm
dijkstra(start)

# print all shortest distances to all the nodes
for i in range(1, n + 1):
    # print "INFINITY" if cannot be reached
    if distance[i] == INF:
        print("INFINITY")
    # print the distance if can be reached
    else:
        print(distance[i])
