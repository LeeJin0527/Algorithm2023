from collections import deque
n, m = map(int, input().split())
q = deque()
graph = []
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == -1:
            q.append([nx, ny])
            graph[nx][ny] = 2
            visited[nx][ny] = visited[x][y] + 1
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            print(0, end = ' ')
        else:
            print(visited[x][y], end = ' ')
    print()