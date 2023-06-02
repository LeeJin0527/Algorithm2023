from collections import deque
n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
taxi = [x-1, y-1]
start_passenger = []
end_passenger = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(m):
	a, b, c, d = map(int, input().split())
	start_passenger.append([a-1, b-1])
	end_passenger.append([c-1, d-1])
def find_passenger(taxi):
	q = deque()
	q.append(taxi)
	visited = [[0] * n for _ in range(n)]
	maxDistance = int(1e9)
	court = []
	while q:
		x, y = q.popleft()
		if visited[x][y] > maxDistance:
			break
		if [x, y] in start_passenger:
			maxDistance = visited[x][y]
			court.append([x, y])
		else:
			for i in range(4):
				nx =  x + dx[i]
				ny =  y + dy[i]
				if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
					visited[nx][ny] = visited[x][y] + 1
					q.append([nx, ny])
	if court:
		court.sort()
		return visited[court[0][0]][court[0][1]], court[0][0], court[0][1]
	else:
		return -1, -1, -1

def go_destination(start, end):
	q = deque()
	q.append(start)
	visited = [[0] * n for _ in range(n)]
	while q:
		x, y = q.popleft()
		if [x, y] == end:
			break
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] != 1:
				q.append([nx, ny])
				visited[nx][ny] = visited[x][y] + 1
	return visited[x][y], x, y
# 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다.
for _ in range(m):
	# 최단거리 고객 찾기
	distance, px, py = find_passenger(taxi)
	# 종료조건
	if fuel - distance < 0 or distance == -1:
		fuel = -1
		break
	# 연료 감소
	fuel -= distance
	idx = start_passenger.index([px, py])
	start_passenger[idx] = [-1, -1]
	# 이동하기
	distacne2, px2, py2 = go_destination([px, py], end_passenger[idx])
	if fuel - distacne2 < 0 or [px2, py2] != end_passenger[idx]:
		fuel = -1
		break
	fuel += distacne2
	taxi = [px2, py2]
print(fuel)

