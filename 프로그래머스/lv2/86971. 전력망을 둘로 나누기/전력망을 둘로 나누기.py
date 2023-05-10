def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
def solution(n, wires):
    answer = int(1e9)
    for index in range(n-1):
        graph = wires[:index] + wires[index+1:]
        parent = [0] * (n+1)
        for i in range(1, n+1):
            parent[i] = i
        
        for x, y in graph:
            if find_parent(parent, x) != find_parent(parent, y):
                union_find(parent, x, y)
        for i in range(1, n+1):
            find_parent(parent, i)
        parent = parent[1:]
        if set(parent) == 1:
            return 0
        else:
            check = list(set(parent))
            one = parent.count(check[0])
            two = parent.count(check[1])
            answer = min(answer, abs(one - two))
    return answer