import sys
input = sys.stdin.readline
t = int(input())
wordsAndCount = []
for _ in range(t):
    wordsAndCount.append([input().rstrip(), int(input())])

for index in range(t):
    shortestLength = int(1e9)
    longestLength = 0
    check = wordsAndCount[index][0]
    maximumSameCount = wordsAndCount[index][1]
    if maximumSameCount == 1:
        print(1, 1)
        continue
    for eachIndex, each in enumerate(check):
        if check.count(each) < maximumSameCount:
            continue
        cnt = 1
        same = 1
        temp = [each]
        for j in range(eachIndex+1, len(check)):
            if check[j] == each:
                same += 1
            temp.append(check[j])
            cnt += 1
            if check[j] == each and same == maximumSameCount:
                break

        if same == maximumSameCount and temp.count(each) == maximumSameCount:
            shortestLength = min(shortestLength, cnt)
            longestLength = max(longestLength, cnt)
    if shortestLength == int(1e9) or longestLength == 0:
        print(-1)
    else:
        print(shortestLength, longestLength)