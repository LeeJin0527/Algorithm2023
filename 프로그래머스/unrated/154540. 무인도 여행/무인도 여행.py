from collections import deque
def solution(maps):
    
    nLength = len(maps)
    mLength = len(maps[0])
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(mLength)] for _ in range(nLength)]
    for x in range(nLength):
        for y in range(mLength):
            if not visited[x][y] and maps[x][y] != 'X':
                visited[x][y] = True
                cnt = int(maps[x][y])
                q = deque()
                q.append([x, y])
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if nx < 0 or ny < 0 or nx >= nLength or ny >= mLength:
                            continue
                        if not visited[nx][ny] and maps[nx][ny] != 'X':
                            q.append([nx, ny])
                            cnt += int(maps[nx][ny])
                            visited[nx][ny] = True
                            
                answer.append(int(cnt))
    if len(answer) == 0:
        return [-1]
    answer.sort()
            
    return answer