n = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxResult, minResult = -1e9, 1e9
def dfs(result, v, add, sub, mul, div):
	global maxResult, minResult
	if v == n:
		maxResult = max(maxResult, result)
		minResult = min(minResult, result)
		return
	else:
		if add:
			dfs(result+lst[v], v+1, add-1, sub, mul, div)
		if sub:
			dfs(result-lst[v], v+1, add, sub-1, mul, div)
		if mul:
			dfs(result*lst[v], v+1, add, sub, mul-1, div)
		if div:
			dfs(int(result/lst[v]), v+1, add, sub, mul, div-1)

dfs(lst[0], 1, add, sub, mul, div)
print(maxResult)
print(minResult)