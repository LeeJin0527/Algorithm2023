import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque()
q.append([n, 0])
result = []
visited = [False] * 100001
while q:
    x, cnt = q.popleft()
    visited[x] = True
    if x > 100000:
        continue
    if x == k:
        result.append(cnt)
    if 0 <= 2*x <= 100000 and not visited[2*x]:
        visited[2*x] = True
        q.append([2*x, cnt])
    if 0 <= x-1 <= 100000 and not visited[x-1]:
        visited[x-1] = True
        q.append([x-1, cnt+1])
    if 0 <= x+1 <= 100000 and not visited[x+1]:
        visited[x+1] = True
        q.append([x+1, cnt+1])
print(min(result))