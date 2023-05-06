scores = []
maxValue = 0
result = 0
for index in range(1, 6):
    scores.append([sum(list(map(int, input().split()))), index])
    if scores[index-1][0] > maxValue:
        maxValue = scores[index-1][0]
        result = index
print(result, maxValue)