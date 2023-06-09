n = int(input())
for _ in range(n):
    check = input().rstrip()
    if 6 <= len(check) <= 9:
        print('yes')
    else:
        print('no')