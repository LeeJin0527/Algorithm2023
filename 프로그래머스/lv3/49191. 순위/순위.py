def solution(n, results):
    answer = 0
    graph = [[-2 for _ in range(n+1)] for _ in range(n+1)]
    for x in range(1, n+1):
        for y in range(1, n+1):
            if x == y:
                graph[x][y] = 0
    for result in results:
        x, y = result
        graph[x][y] = 1
        graph[y][x] = 0
        
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if graph[x][k] == 1 and graph[k][y] == 1:
                    graph[x][y] = 1
                    graph[y][x] = 0
                elif graph[x][k] == 0 and graph[k][y] == 0:
                    graph[x][y] = 0
                    graph[y][x] = 1
    for index in range(1, n+1):
        check = graph[index][1:]
        if -2 not in check:
            answer += 1

    return answer