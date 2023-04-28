t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    maxValue = stocks[-1]
    answer = 0
    for index in range(len(stocks)-1, -1, -1):
        if stocks[index] > maxValue:
            maxValue = stocks[index]
        else:
            answer += maxValue - stocks[index]
    print(answer)
