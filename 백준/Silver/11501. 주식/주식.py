import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    maxNumber = 0
    answer = 0
    for index in range(n-1, -1, -1):
        if numbers[index] > maxNumber:
            maxNumber = numbers[index]
        else:
            answer += maxNumber - numbers[index]
    print(answer)
