n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []
chess = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y, z = map(int, input().split())
    horse.append([x-1, y-1, z-1])
    chess[x-1][y-1].append(i)
def change_dir(d):
	if d in [0, 2]:
		d += 1
	elif d in [1, 3]:
		d -= 1
	return d

def solve(horse_num):
    x, y, d = horse[horse_num]
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
        d = change_dir(d)
        horse[horse_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
            return True
    horse_add = []
    for i, v in enumerate(chess[x][y]):
        if v == horse_num:
            horse_add.extend(chess[x][y][i:])
            chess[x][y] = chess[x][y][:i]
            break
    if graph[nx][ny] == 1:
        horse_add = horse_add[-1::-1]
    for h in horse_add:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)
    if len(chess[nx][ny]) >= 4:
        return False
    return True
cnt = 0
while True:
    flag = False
    if cnt > 1000:
        print(-1)
        exit()
    for i in range(k):
        if solve(i) == False:
            flag = True
            break
    cnt += 1
    if flag:
        print(cnt)
        break