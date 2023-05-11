import heapq
def solution(n, vertex):
    answer = 0
    distance = [int(1e9) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for vert in vertex:
        x, y = vert
        graph[x].append([y, 1])
        graph[y].append([x, 1])
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, [0, start])
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, [cost, i[0]])
    dijkstra(1)
    distance = distance[1:]
    check = max(distance)
    for dist in distance:
        if dist == check:
            answer += 1
    
    return answer