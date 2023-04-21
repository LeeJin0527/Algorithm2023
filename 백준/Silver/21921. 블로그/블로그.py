n, x = map(int, input().split())
visiters = list(map(int, input().split()))
end = 0
intervalSum = 0
currentCount = 0
maxValue = sum(visiters[0: x])
cnt = 0
for start in range(n):
    while end < n and currentCount < x:
        intervalSum += visiters[end]
        end += 1
        currentCount += 1
    if currentCount == x:
        if intervalSum > maxValue:
            maxValue = intervalSum
            cnt = 1
        elif intervalSum == maxValue:
            cnt += 1
        intervalSum -= visiters[start]
        currentCount -= 1
if maxValue == 0:
    print('SAD')
else:
    print(maxValue)
    print(cnt)