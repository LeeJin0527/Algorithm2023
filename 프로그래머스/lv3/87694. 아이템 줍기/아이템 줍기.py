from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    visited = [[False for _ in range(102)] for _ in range(102)]
    graph = [[0 for _ in range(102)] for _ in range(102)]
    for rect in rectangle:
        y1, x1, y2, x2 = rect[0] * 2, rect[1] * 2, rect[2] * 2, rect[3] * 2
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                graph[x][y] = 1
    for rect in rectangle:
        y1, x1, y2, x2 = rect[0] * 2, rect[1] * 2, rect[2] * 2, rect[3] * 2
        for x in range(min(x1, x2)+1, max(x1, x2)):
            for y in range(min(y1, y2) +1, max(y1, y2)):
                graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([characterY*2, characterX*2])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 102 or ny >= 102:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

    return graph[itemY*2][itemX*2] // 2