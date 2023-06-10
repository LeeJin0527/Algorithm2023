def dfs(portion, res, visited, target, dungeons):
    global answer
    if res > answer:
        answer = res 
    for i in range(target):
        if portion >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(portion - dungeons[i][1], res + 1, visited, target, dungeons)
            visited[i] = False
    
def solution(k, dungeons):
    global answer
    n = len(dungeons)
    visited = [False for _ in range(n)]
    dfs(k, 0, visited, n, dungeons)
    return answer
answer = 0