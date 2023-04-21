import sys
input = sys.stdin.readline
n, m = map(int, input().split())
check = []
for _ in range(n):
    tmp = input().rstrip().split()
    check.append([tmp[0], int(tmp[1])])
for index in range(m):
    start, end = 0, n-1
    answer = ''
    number = int(input())
    while start <= end:
        mid = (start + end) // 2
        if number <= check[mid][1]:
            end = mid - 1
            answer = check[mid][0]
        else:
            start = mid + 1
    print(answer)