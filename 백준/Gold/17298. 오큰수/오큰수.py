import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [-1] * len(numbers)
for index, value in enumerate(numbers):
    while stack and numbers[stack[-1]] < value:
        answer[stack.pop()] = value
    stack.append(index)
print(*answer)
