from collections import deque
def bfs(video, compare, visited):
    q = deque()
    q.append([video, int(1e9)])
    visited[video] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        for each in graph[x]:
            # 관련된 그래프 번호와 비용
            nx, ny = each
            checkMin = min(ny, y)
            if not visited[nx] and checkMin >= compare:
                visited[nx] = True
                q.append([nx, checkMin])
                cnt += 1
    answer.append(cnt)
n, m = map(int, input().split())
answer = []
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, c = map(int, input().split())
    graph[x].append([y, c])
    graph[y].append([x, c])
for _ in range(m):
    k, start = map(int, input().split())
    visited = [False] * (n+1)
    bfs(start, k, visited)
for ans in answer:
    print(ans)