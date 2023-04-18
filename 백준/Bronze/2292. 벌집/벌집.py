n = int(input())
start = 1
temp, pre = 1, 0
cnt = 1
if n == 1:
    print(1)
    exit()
while True:
    pre = temp + 1
    temp += (6 * cnt)
    cnt += 1
    if pre <= n <= temp:
        print(cnt)
        break
