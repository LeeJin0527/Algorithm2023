from itertools import permutations
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
for l in list(permutations(lst, n)):
    flag = True
    value = 500
    for each in l:
        value += each
        value -= k
        if value < 500:
            flag = False
            break
    if flag:
        answer += 1
print(answer)