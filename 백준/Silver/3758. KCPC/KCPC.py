T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    questionNumbersAndScores = [[[] for _ in range(k+1)] for _ in range(n+1)]
    submitCounts = [0 for _ in range(n+1)]
    submitTime = [int(1e9) for _ in range(n+1)]
    for index in range(1, m+1):
        teamID, questionNumber, score = map(int, input().split())
        submitCounts[teamID] += 1
        submitTime[teamID] = index
        questionNumbersAndScores[teamID][questionNumber].append(score)
    result = []
    for index, question in enumerate(questionNumbersAndScores):
        tmp = 0
        for each in question:
            if each:
               tmp += max(each)
        result.append([index, tmp])
    for i in range(len(result)):
        result[i].append(submitCounts[i])
        result[i].append(submitTime[i])
    result = result[1:]
    result.sort(key=lambda x:(-x[1], x[2], x[3]))
    rank = 1
    for res in result:
        if res[0] == t:
            print(rank)
            break
        rank += 1