import copy
def dfs(graph, res_x, res_y, position, num, visited):
    visited[res_x][res_y] = True
    res = [position]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for index in range(4):
        nx = res_x + dx[index]
        ny = res_y + dy[index]
        if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
            continue
        if graph[nx][ny] == num and not visited[nx][ny]:
            graph[nx][ny] = 2
            visited[nx][ny] = True
            res = res + dfs(graph, nx, ny, [position[0] + dx[index], position[1] + dy[index]], num, visited)
    return res

def rotate(lst):
    res = list(map(list, zip(*lst[::-1])))
    return res

def solution(game_board, table):
    answer = 0
    blocks = []
    n = len(game_board)
    boardVisited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == 0 and not boardVisited[x][y]:
                game_board[x][y] = 2
                result = dfs(game_board, x, y, [0, 0], 0, boardVisited)
                blocks.append(result)

    for _ in range(4):
        tableVisited = [[False] * n for _ in range(n)]
        table = rotate(table)
        table_copy = copy.deepcopy(table)
        for x in range(n):
            for y in range(n):
                if table_copy[x][y] == 1 and not tableVisited[x][y]:
                    table_copy[x][y] = 2
                    temp = dfs(table_copy, x, y, [0, 0], 1, tableVisited)
                    if temp in blocks:
                        answer += len(temp)
                        blocks.remove(temp)
                        table = copy.deepcopy(table_copy)
                    else:
                        table_copy = copy.deepcopy(table)
    return answer