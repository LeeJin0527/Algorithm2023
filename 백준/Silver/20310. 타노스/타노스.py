import sys
input = sys.stdin.readline
elements = list(map(int, input().rstrip()))
oneCount = elements.count(1)
zeroCount = elements.count(0) // 2

n = len(elements)

candidate = []
for index in range(len(elements)):
    if elements[index] == 0 and zeroCount > 0:
        zeroCount -= 1
        candidate.append(0)


fillOneToTheRight = len(elements) // 2 - len(candidate)
for _ in range(fillOneToTheRight):
    candidate.append(1)
candidate = list(map(str, candidate))
print(''.join(candidate))

