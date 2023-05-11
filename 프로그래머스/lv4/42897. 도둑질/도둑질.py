def solution(money):
    answer = 0
    money1 = [0] + money[:-1]
    money2 = [0] + money[1:]
    dp1 = [0 for _ in range(len(money))] 
    dp2 = [0 for _ in range(len(money))] 
    dp1[0] = money1[0]
    dp1[1] = max(money1[0], money1[1])
    dp2[0] = money2[0]
    dp2[1] = max(money2[0], money2[1])
    for index in range(2, len(money1)):
        dp1[index] = max(dp1[index-2] + money1[index], dp1[index-1])
    for index in range(2, len(money2)):
        dp2[index] = max(dp2[index-2] + money2[index], dp2[index-1])

    return max(dp1[-1], dp2[-1])