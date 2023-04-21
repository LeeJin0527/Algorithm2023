from collections import defaultdict
n, m = map(int, input().split())
countCheck = defaultdict(int)
resultCheck = []
for i in range(n):
    candidate = input().rstrip()
    if len(candidate) < m:
        continue
    countCheck[candidate] += 1
for count in countCheck:
    resultCheck.append([countCheck[count], len(count), count])
resultCheck.sort(key=lambda x: (-x[0], -x[1], x[2]))
for result in resultCheck:
    print(result[2])