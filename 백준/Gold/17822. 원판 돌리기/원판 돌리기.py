from copy import deepcopy
n, m, t = map(int, input().split())
board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

def rotate(x, d, k):
	# 회전
	for i in range(x-1, n, x):
		temp = [0] * m
		if d == 0:
			for j in range(m):
				# 시계 방향 회전
				temp[j] = board[i][(j-k+m) % m]
		else:
			for j in range(m):
				temp[j] = board[i][(j+k+m) % m]
		board[i] = temp


def remove():
	global board
	temp = deepcopy(board)
	for i in range(n):
		for j in range(m):
			if board[i][j] == -1: continue
			if board[i][(j - 1 + m) % m] == board[i][j]:
				temp[i][j] = -1
				temp[i][(j - 1 + m) % m] = -1
			if board[i][(j + 1 + m) % m] == board[i][j]:
				temp[i][j] = -1
				temp[i][(j + 1 + m) % m] = -1
	for j in range(m):
		for i in range(1, n):
			if board[i][j] == -1: continue
			if board[i-1][j] == board[i][j]:
				temp[i][j] = -1
				temp[i-1][j] = -1
	if board == temp:
		return False
	board = temp
	return True

def calcAverage():
	avg = 0
	cnt = 0
	for i in range(n):
		for j in range(m):
			if board[i][j] != -1:
				avg += board[i][j]
				cnt += 1
	if cnt == 0:
		return
	avg /= cnt
	for i in range(n):
		for j in range(m):
			if board[i][j] != -1:
				if board[i][j] > avg:
					board[i][j] -= 1
				elif board[i][j] < avg:
					board[i][j] += 1

for _ in range(t):
	x, d, k = map(int, input().split())
	rotate(x, d, k)
	check = remove()
	if not check:
		calcAverage()
result = 0
for i in range(n):
	for j in range(m):
		if board[i][j] != -1:
			result += board[i][j]
print(result)

