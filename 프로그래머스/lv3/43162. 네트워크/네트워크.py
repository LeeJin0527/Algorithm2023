def dfs(v, visited, graph):
    visited[v] = True
    for index in range(len(graph[v])):
        if not visited[index] and graph[v][index] == 1:
            visited[index] = True
            dfs(index, visited, graph)
                       
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for index in range(n):
        if not visited[index]:
            dfs(index, visited, computers)
            answer += 1
    return answer