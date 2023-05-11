from collections import defaultdict
def dfs(check, path, airports, visited, n):
    global answer
    if len(path) == n+1:
        answer.append(path)
    for index, airport in enumerate(airports[check]):
        if not visited[check][index]:
            visited[check][index] = True
            dfs(airport, path + [airport], airports, visited, n)
            visited[check][index] = False
    
def solution(tickets):
    global answer
    airports = defaultdict(list)
    visited = defaultdict(list)
    
    for ticket in tickets:
        start, end = ticket
        airports[start].append(end)
        visited[start].append(False)

    dfs("ICN", ["ICN"], airports, visited, len(tickets))

    answer.sort()
    return answer[0]
answer = []