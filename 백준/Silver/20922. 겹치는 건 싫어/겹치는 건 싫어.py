import sys
from collections import defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())
elements = list(map(int, input().split()))
start, end = 0, 0
check = defaultdict(int)
result = 0
while end < n:
    if check[elements[end]] < k:
        check[elements[end]] += 1
        end += 1
    else:
        check[elements[start]] -= 1
        start += 1
    result = max(result, end - start)
print(result)