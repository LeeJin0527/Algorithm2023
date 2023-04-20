from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    playerCount = defaultdict(int)
    for l in lst:
        playerCount[l] += 1
    compare = defaultdict(list)
    temp = 1
    for index, value in enumerate(lst):
        if playerCount[value] != 6:
            continue
        compare[value].append(temp)
        temp += 1
    result = []
    for index, value in enumerate(compare):
        compare[value].sort()
        result.append([value, sum(compare[value][:4]), compare[value][4]])
    result.sort(key=lambda x: (x[1], x[2]))
    print(result[0][0])

