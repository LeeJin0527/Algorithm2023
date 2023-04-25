n = int(input())
storages = []
checkHeight = []
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    storages.append([a, b])
storages.sort()
for storage in storages:
    checkHeight.append(storage[1])
cur_x, cur_y = storages[0][0], storages[0][1]
for index in range(len(storages)):
    if storages[index][0] > cur_x and storages[index][1] >= cur_y:
        answer += cur_y * (storages[index][0] - cur_x)
        cur_x = storages[index][0]
        cur_y = storages[index][1]
    try:
        if storages[index][1] > max(checkHeight[index + 1:]):
            cur_x = storages[index][0] + 1
            cur_y = max(checkHeight[index + 1:])

            answer += storages[index][1]
    except:
        pass
    if index == len(storages) - 1:
        answer += storages[-1][1]

print(answer)
