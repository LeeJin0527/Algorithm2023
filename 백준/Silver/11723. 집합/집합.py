import sys
input = sys.stdin.readline
lst = set()
m = int(input())
for _ in range(m):
    compare = list(input().split())
    if compare[0] == 'add':
        lst.add(int(compare[1]))
    elif compare[0] == 'remove':
        if int(compare[1]) in lst:
            lst.discard(int(compare[1]))
    elif compare[0] == 'check':
        if int(compare[1]) in lst:
            print(1)
        else:
            print(0)
    elif compare[0] == 'toggle':
        if int(compare[1]) in lst:
            lst.discard(int(compare[1]))
        else:
            lst.add(int(compare[1]))
    elif compare[0] == 'all':
        lst = set(i for i in range(1, 21))
    elif compare[0] == 'empty':
        lst = set()

