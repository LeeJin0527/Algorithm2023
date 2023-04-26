import sys
input = sys.stdin.readline
elements = list(map(int, input().rstrip()))
oneCount = elements.count(1) // 2
zeroCount = elements.count(0) // 2

n = len(elements)

zeroFill = []
oneFill = []
result = []
for index in range(len(elements)):
    if elements[index] == 0 and zeroCount > 0:
        zeroCount -= 1
        zeroFill.append(index)
for index in range(len(elements)-1, -1, -1):
    if elements[index] == 1 and oneCount > 0:
        oneCount -= 1
        oneFill.append(index)
for value in range(n):
    if value in zeroFill:
        result.append(0)
    if value in oneFill:
        result.append(1)
result = list(map(str, result))
print(''.join(result))
