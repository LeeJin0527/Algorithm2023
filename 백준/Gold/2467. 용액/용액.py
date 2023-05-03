import sys
input = sys.stdin.readline
n = int(input())
solution = list(map(int, input().split()))
answer = 2*int(1e9)
start, end = 0, n-1
result = [solution[start], solution[end]]
while start < end:
    if solution[start] * solution[end] < 0:
        check = solution[start] + solution[end]
    else:
        if solution[start] < 0 and solution[end] < 0:
            check = solution[start] - solution[end]
        elif solution[start] > 0 and solution[end] > 0:
            check = solution[start] + solution[end]
    if answer > abs(check):
        result = [solution[start], solution[end]]
        answer = abs(check)
    if check > 0:
        end -= 1
    else:
        start += 1
result.sort()
print(*result)