def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_find(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x
        
def solution(n, costs):
    answer = 0
    parent = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        parent[i] = i
    costs.sort(key=lambda x: x[2])
    for cost in costs:
        x, y, c = cost
        if find_parent(parent, x) != find_parent(parent, y):
            union_find(parent, x, y)
            answer += c

    return answer