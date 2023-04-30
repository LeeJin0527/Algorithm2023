from collections import deque
import sys
input = sys.stdin.readline
start = input().rstrip()
target = input().rstrip()
q = deque()
q.append(target)
check = set()
check.add(target)
flag = True
while q:
    x = q.popleft()
    if x == start:
        print(1)
        flag = False
        break
    check.add(x)
    if x:
        if x[::-1][-1] == 'B':
            reverseAndDeleteLastElement = x[::-1][:-1]
            if reverseAndDeleteLastElement not in check:
                check.add(reverseAndDeleteLastElement)
                q.append(reverseAndDeleteLastElement)
        if x[-1] == 'A':
            deleteLastElement = x[:-1]
            if deleteLastElement not in check:
                check.add(deleteLastElement)
                q.append(deleteLastElement)

if flag:
    print(0)