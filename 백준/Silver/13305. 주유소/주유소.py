n = int(input())
distances = list(map(int, input().split()))
oilBank = list(map(int, input().split()))
cost = 0
for index, value in enumerate(distances):
    if index == 0:
        cost += value * oilBank[index]
    else:
        cost += value * min(oilBank[:index+1])
print(cost)