n, q = map(int, input().split())
graph = []
for _ in range(2**n):
	graph.append(list(map(int, input().split())))
step = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(start):
	q = []
	q.append(start)
	cnt = 1
	while q:
		x, y = q[0]
		q.pop(0)
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= (2**n) or ny >= (2**n):
				continue
			if graph[nx][ny] > 0 and not visited[nx][ny]:
				visited[nx][ny] = True
				q.append([nx, ny])
				cnt += 1
	return cnt

for s in step:
	k = 2 ** s
	rotate = [[0] * (2**n) for _ in range(2**n)]
	for i in range(0, 2**n, k):
		for j in range(0, 2**n, k):
			for x in range(k):
				for y in range(k):
					rotate[i + y][j + k - x - 1] = graph[i+x][j+y]
	ice_turn = [[0] * (2**n) for _ in range(2**n)]
	for x in range(2**n):
		for y in range(2**n):
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if 0 <= nx < (2**n) and 0 <= ny < (2**n) and rotate[nx][ny] != 0:
					ice_turn[x][y] += 1
	graph = [[0] * (2**n) for _ in range(2**n)]
	for x in range(2**n):
		for y in range(2**n):
			if rotate[x][y] > 0:
				if ice_turn[x][y] < 3:
					graph[x][y] = rotate[x][y] -1
				else:
					graph[x][y] = rotate[x][y]
answer = 0
visited = [[False] * (2**n) for _ in range(2**n)]
for i in range(2**n):
	for j in range(2**n):
		if graph[i][j] > 0:
			answer += graph[i][j]
print(answer)
value = 0
for i in range(2**n):
	for j in range(2**n):
		if not visited[i][j] and graph[i][j] != 0:
			visited[i][j] = True
			value = max(value, dfs([i, j]))
print(value)

