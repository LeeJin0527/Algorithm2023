def solution(n, results):
    answer = 0
    graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    for x in range(1, n+1):
        graph[x][x] = -2
    for result in results:
        x, y = result
        graph[x][y] = 1
        graph[y][x] = 0
        
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if graph[x][k] == 1 and graph[k][y] == 1:
                    graph[x][y] = 1
                if graph[x][k] == 0 and graph[k][y] == 0:
                    graph[x][y] = 0
    for index in range(1, len(graph)):
        graph[index] = graph[index][1:]
        if -1 not in graph[index]:
            answer += 1
    return answer