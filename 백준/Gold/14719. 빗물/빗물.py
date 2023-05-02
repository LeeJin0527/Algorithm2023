n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
for i in range(1, m-1):
	left = lst[:i]
	right = lst[i+1:]
	block = min(max(left), max(right))
	if block > lst[i]:
		answer += block-lst[i]
print(answer)
