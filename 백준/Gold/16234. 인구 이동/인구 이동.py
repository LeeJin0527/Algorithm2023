import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    pass

input = sys.stdin.readline
n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def bfs(a, b):
    q = deque()
    q.append([a, b])
    temp = []
    temp.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp



cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum(board[x][y] for x, y in temp) // len(temp)
                    for x, y in temp:
                        board[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)