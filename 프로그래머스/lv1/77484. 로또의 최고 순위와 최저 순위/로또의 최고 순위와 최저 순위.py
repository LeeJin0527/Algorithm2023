def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zeroCount = 0
    for index, value in enumerate(lottos):
        if value in win_nums:
            cnt += 1
        if value == 0:
            zeroCount += 1

    maxRank = cnt + zeroCount
    if maxRank >= 6:
        answer.append(1)
    elif maxRank < 2:
        answer.append(6)
    else:
        answer.append(6 - maxRank + 1)
        
    minRank = cnt
    if minRank < 2:
        answer.append(6)
    else:
        answer.append(6 - minRank + 1)

    return answer