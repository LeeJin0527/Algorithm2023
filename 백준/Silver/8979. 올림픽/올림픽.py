n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = 1
if lst[0][0] == k:
    print(1)
else:
    temp = lst[0][1:]
    for index in range(1, len(lst)):
        if lst[index][0] == k:
            print(rank)
            break
        if temp != lst[index][1:]:
            rank += 1
            temp = lst[index][1:]
