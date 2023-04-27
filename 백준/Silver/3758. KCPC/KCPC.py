import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    submitCount = [0] * (n+1)
    lastSubmit = [0] * (n+1)
    scores = [0] * (n+1)
    result = []
    kcpc = [[[] for _ in range(k+1)] for _ in range(n+1)]
    for index in range(m):
        teamID, number, score = map(int, input().split())
        submitCount[teamID] += 1
        lastSubmit[teamID] = index
        kcpc[teamID][number].append(score)
    for index in range(1, len(kcpc)):
        check = kcpc[index]
        for number in range(len(check)):
            if check[number]:
                kcpc[index][number] = [max(kcpc[index][number])]
    for index, team in enumerate(kcpc):
        temp = 0
        for each in team:
            if each:
                temp += each[0]
        scores[index] = temp

    for index in range(n+1):
        result.append([scores[index], submitCount[index], lastSubmit[index], index])
    result.sort(key = lambda x: (-x[0], x[1], x[2]))
    rank = 1
    for index in range(len(result)):
        if result[index][-1] == t:
            print(rank)
            break
        rank += 1

