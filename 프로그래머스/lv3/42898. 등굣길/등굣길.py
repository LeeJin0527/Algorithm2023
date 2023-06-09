def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] in puddles:
                dp[x][y] = 0
                continue
            elif x == 1 and y == 1:
                continue
            else:
                dp[x][y] = (dp[x-1][y] + dp[x][y-1]) % 1000000007
    return dp[-1][-1]