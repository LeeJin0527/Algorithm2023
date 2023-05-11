def dfs(value, graph, visited):
    visited[value] = True
    for index in range(len(graph[value])):
        if not visited[index] and graph[value][index] == 1:
            dfs(index, graph, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for index in range(n):
        if not visited[index]:
            dfs(index, computers, visited)
            answer += 1
    return answer