r, c, t = map(int, input().split())
graph = []
for _ in range(r):
	graph.append(list(map(int, input().split())))
for i in range(r):
	if graph[i][0] == -1:
		top = i
		down = i + 1
		break
def expand():
	tmp_graph = [[0] * c for _ in range(r)]
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	for x in range(r):
		for y in range(c):
			tmp = 0
			if graph[x][y] > 0:
				for i in range(4):
					nx = x + dx[i]
					ny = y + dy[i]
					if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
						tmp_graph[nx][ny] += graph[x][y] // 5
						tmp += graph[x][y] // 5
				graph[x][y] -= tmp
	for x in range(r):
		for y in range(c):
			graph[x][y] += tmp_graph[x][y]

# 반시계 동 북 서 남
def upClean():
	dx = [0, -1, 0, 1]
	dy = [1, 0, -1, 0]
	direction = 0
	before = 0
	x, y = top, 1
	while True:
		if x == top and y == 0:
			break
		nx = x + dx[direction]
		ny = y + dy[direction]
		if nx < 0 or ny < 0 or nx >= r or ny >= c:
			direction += 1
			continue
		graph[x][y], before = before, graph[x][y]
		x, y = nx, ny







# 시계 동 남 서 북
def downClean():
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	direction = 0
	before = 0
	x, y = down , 1
	while True:
		if x == down and y == 0:
			break
		nx = x + dx[direction]
		ny = y + dy[direction]
		if nx < 0 or ny < 0 or nx >= r or ny >= c:
			direction += 1
			continue
		graph[x][y], before = before, graph[x][y]
		x, y = nx, ny


for _ in range(t):
	expand()
	upClean()
	downClean()

answer = 0
for i in range(r):
	for j in range(c):
		if graph[i][j] > 0:
			answer += graph[i][j]
print(answer)