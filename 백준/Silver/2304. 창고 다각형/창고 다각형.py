n = int(input())
storages = []
maxX = 0
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    storages.append([a, b])
    maxX = max(maxX, a)
checkHeight = [0 for _ in range(maxX+1)]
for storage in storages:
    x, y = storage
    checkHeight[x] = y
standard = checkHeight.index(max(checkHeight))
startLeft = 0
startRight = checkHeight[-1]
for left in range(standard+1):
    if checkHeight[left] > startLeft:
        startLeft = checkHeight[left]
    answer += startLeft
for right in range(len(checkHeight)-1, standard, -1):
    if checkHeight[right] > startRight:
        startRight = checkHeight[right]
    answer += startRight
print(answer)