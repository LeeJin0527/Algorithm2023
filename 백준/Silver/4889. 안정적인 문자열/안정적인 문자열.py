testCase = 1
import sys
while True:
    stack = []
    cnt = 0
    lst = sys.stdin.readline().rstrip()
    if '-' in lst:
        break

    lst = list(lst)
    for l in lst:
        if len(stack) == 0 and l == '}':
            cnt += 1
            stack.append('{')
        elif stack and l == '}':
            stack.pop()
        else:
            stack.append(l)
    cnt += len(stack) // 2
    print(f'{testCase}. {cnt}')
    testCase += 1
