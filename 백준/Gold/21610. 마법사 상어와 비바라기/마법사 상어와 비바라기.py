n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append([a-1, b])

#  dir
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 대각선
sx = [-1, -1, 1, 1]
sy = [-1, 1, -1, 1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for d, s in lst:
    # 1, 모든 구름이 d s 이동
    moved_clouds = []
    for x, y in clouds:
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        board[nx][ny] += 1
        moved_clouds.append((nx, ny))

    for x, y in moved_clouds:
        cnt = 0
        for i in range(4):
            nx = x + sx[i]
            ny = y + sy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if (x, y) in moved_clouds or board[x][y] < 2:
                continue
            board[x][y] -= 2
            new_clouds.append((x, y))
    clouds = new_clouds
result = 0
for i in range(n):
    for j in range(n):
        result += board[i][j]
print(result)


