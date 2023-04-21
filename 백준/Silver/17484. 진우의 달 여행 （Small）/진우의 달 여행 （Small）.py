from collections import deque
n, m = map(int, input().split())
graph = []
result = int(1e9)
for _ in range(n):
    graph.append(list(map(int, input().split())))
q = deque()
dx = [1, 1, 1]
dy = [-1, 0, 1]
for index in range(m):
    q.append([0, index, 1, graph[0][index], -1])
while q:
    x, y, cnt, res, dir = q.popleft()
    if cnt == n:
        result = min(result, res)
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if i != dir:
            q.append([nx, ny, cnt+1, res + graph[nx][ny], i])
print(result)