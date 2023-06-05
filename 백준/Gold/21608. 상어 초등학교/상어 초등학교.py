import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
lst = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
lst = defaultdict(list)
for _ in range(n**2):
    x = (list(map(int, input().split())))
    lst[x[0]] = x[1:]

board = [[0] * (n+1) for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]


for l in lst:

    # 비어 있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
    # 1을 만족하는 칸이 여러개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다
    # 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로 , 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸
    sumList = defaultdict(list)
    for i in range(1, n+1):
        for j in range(1, n+1):
            x, y = i, j
            if board[x][y] != 0:
               continue
            cnt = 0
            like = 0
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                if board[nx][ny] in lst[l]:
                    like += 1
                if board[nx][ny] == 0:
                    cnt += 1
            # print(like, cnt, x, y)
            sumList[like * 10 + cnt * 1].append([x, y])

    board[sumList[max(sumList)][0][0]][sumList[max(sumList)][0][1]] = l


result = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt = 0
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue

            if board[nx][ny] in lst[board[i][j]]:
                cnt += 1

        if cnt == 0:
            result += 0
        else:
            result += 10** ( cnt-1)
print(result)
