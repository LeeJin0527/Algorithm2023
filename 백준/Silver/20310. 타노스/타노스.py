from collections import defaultdict
check = defaultdict(int)
datas = input().rstrip()
for data in datas:
    check[data] += 1
result = []
for che in check:
    tmp = check[che] // 2
    for _ in range(tmp):
        result.append(che)
result.sort()
print(''.join(result))