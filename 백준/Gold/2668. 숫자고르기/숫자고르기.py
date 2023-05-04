import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
check = []
result = []
for _ in range(n):
    check.append(int(input()))
for index in range(1, n+1):
    graph[check[index-1]].append(index)
def dfs(origin, v):
    for each in graph[v]:
        if each == origin:
            result.append(origin)
            return
        dfs(origin, each)
for index in range(1, n+1):
    dfs(index, index)
result.sort()
print(len(result))
for res in result:
    print(res)