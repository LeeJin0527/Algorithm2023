import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int, input().split()))
answer = []
stacks = []
for index, value in enumerate(tops):
    while stacks:
        if stacks[-1][1] > value:
            answer.append(stacks[-1][0] + 1)
            break
        else:
            stacks.pop()
    if len(stacks) == 0:
        answer.append(0)
    stacks.append([index, value])
print(*answer)
