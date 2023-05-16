from collections import deque
def solution(x, y, n):
    answer = -1
    visited = []
    q = deque()
    q.append([y, 0])
    while q:
        y, result = q.popleft()
        if x == y:
            return result
        if y < 0:
            continue
        q.append([y - n, result + 1])
        if y % 2 == 0:
            q.append([y // 2, result + 1])
        if y % 3 == 0:
            q.append([y // 3, result + 1])
    return answer