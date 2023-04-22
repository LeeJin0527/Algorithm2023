import copy
from collections import defaultdict
n = int(input())
origin = list(input().rstrip())

cnt = 0
for _ in range(n-1):
    checkCopy = copy.deepcopy(origin)
    compare = list(input().rstrip())
    if len(compare) > len(checkCopy):
        for check in checkCopy:
            if check in compare:
                compare.remove(check)
        if len(compare) == 1 or len(compare) == 0:
            cnt += 1
    else:
        for comp in compare:
            if comp in checkCopy:
                checkCopy.remove(comp)
        if len(checkCopy) == 1 or len(checkCopy) == 0:
            cnt += 1
print(cnt)
