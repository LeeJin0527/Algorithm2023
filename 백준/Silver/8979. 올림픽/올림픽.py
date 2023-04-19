import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))


answer = sorted(lst, key=lambda x: (-x[1], -x[2], -x[3]))

tmp = []
rank = 0
for i in range(n):
	if answer[i][1:] not in tmp:
		tmp.append(answer[i][1:])
		rank += 1
	if answer[i][0] == k:
		print(rank)
		break

