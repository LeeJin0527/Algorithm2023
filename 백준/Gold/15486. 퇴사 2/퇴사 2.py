n = int(input())
period = []
cost = []
for _ in range(n):
    x, y = map(int, input().split())
    period.append(x)
    cost.append(y)
dp = [0 for _ in range(n+1)]
for x in range(n-1, -1, -1):
    if x + period[x] <= n:
        dp[x] = max(dp[x+1], (cost[x] + dp[x + period[x]]))
    else:
        dp[x] = dp[x+1]

print(dp[0])