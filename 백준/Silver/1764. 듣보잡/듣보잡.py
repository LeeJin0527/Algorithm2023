from collections import defaultdict
check = defaultdict(int)
n, m = map(int, input().split())
for _ in range(n):
    person = input().rstrip()
    check[person] += 1
for _ in range(m):
    person = input().rstrip()
    check[person] += 1
answer = 0
result = []
for che in check:
    if check[che] == 2:
        answer += 1
        result.append(che)
print(answer)
result.sort()
for res in result:
    print(res)