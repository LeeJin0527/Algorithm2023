import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)] * (n+1)
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append([y, cost])
    graph[y].append([x, cost])
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(1)
print(distance[n])