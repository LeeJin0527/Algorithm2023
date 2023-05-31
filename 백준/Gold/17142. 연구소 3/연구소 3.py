from itertools import combinations
from collections import deque
n, m = map(int, input().split())
graph = []
check = []
wallCnt = 0
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] == 2:
            check.append([x, y])
        if graph[x][y] == 1:
            wallCnt += 1
viruses = list(combinations(check, m))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(virus):
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for x, y in virus:
        q.append([x, y])
        visited[x][y] = 0
    answer = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                answer = max(answer, visited[nx][ny])
            elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    cnt = 0
    for visit in visited:
        cnt += visit.count(-1)
    if cnt == wallCnt:
        return answer
    return int(1e9)


answer = int(1e9)
for virus in viruses:
    answer = min(answer, bfs(virus))
if answer == int(1e9):
    print(-1)
else:
    print(answer)