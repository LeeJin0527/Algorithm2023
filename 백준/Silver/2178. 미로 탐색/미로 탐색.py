n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = []
    q.append([x, y])
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])
    return board[n-1][m-1]
print(bfs(0, 0))