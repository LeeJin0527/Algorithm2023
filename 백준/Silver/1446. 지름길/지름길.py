import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
distance = [INF] * (10001)
for _ in range(n):
    x, y, c = map(int, input().split())
    graph[x].append([y, c])
for index in range(d):
    graph[index].append([index+1, 1])
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(0)
print(distance[d])