def solution(triangle):
    answer = 0
    graph = []
    for tri in triangle:
        graph.append([0] + tri + [0])

    for index in range(1, len(graph)):
        for i in range(1, len(graph[index])-1):
            temp = max(graph[index][i] + graph[index-1][i-1], graph[index][i] + graph[index-1][i])
            graph[index][i] = temp
    return max(graph[-1])