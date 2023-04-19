n = int(input())
lst = []
for index in range(n):
    x, y = map(int, input().split())
    lst.append([index, x, y])
for l in lst:
    rank = 1
    for j in lst:
        if l[1] < j[1] and l[2] < j[2]:
            rank += 1
    print(rank, end = ' ')