n = 0
visited = []
answer = 0
def dfs(check, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(n):
        if visited[j] == 0 and check >= dungeons[j][0]:
            visited[j] = 1
            dfs(check - dungeons[j][1], cnt +1 , dungeons)
            visited[j] = 0
def solution(k, dungeons):
    global answer
    global n
    global visited
    n = len(dungeons)
    visited = [0] * n
    dfs(k, 0, dungeons)
    return answer