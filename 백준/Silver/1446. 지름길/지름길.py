import heapq
n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
distance = [int(1e9)] * 10001

for _ in range(n):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
for index in range(d+1):
    graph[index].append([index+1, 1])
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(0)
print(distance[d])