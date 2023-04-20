n, value, p = map(int, input().split())
if n == 0:
    print(1)
    exit()
scores = list(map(int, input().split()))
cnt = 0
if min(scores) >= value:
    cnt = len(scores) + 1
    if cnt > p:
        print(-1)
        exit()
for score in scores:
    if score < value:
        break
    cnt += 1
scores.insert(cnt, value)
scores = scores[:p]
for x in scores:
    rank = 1
    for y in scores:
        if x < y:
            rank += 1
    if x == value:
        print(rank)
        break