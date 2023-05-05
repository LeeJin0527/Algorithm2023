import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
answer = A - B
if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    answer = list(answer)
    answer.sort()
    print(*answer)