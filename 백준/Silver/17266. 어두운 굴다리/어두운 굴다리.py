n = int(input())
m = int(input())
lights = list(map(int, input().split()))
lights.sort()
if len(lights) == 1:
    print(max(n - lights[0], lights[0] - 0))
else:
    first = lights[0] - 0
    last = n - lights[-1]
    check = 0
    for i in range(1, len(lights)-1):
        tmp = lights[i] - lights[i-1]
        if tmp % 2 == 0:
            check = max(check, tmp // 2)
        else:
            check = max(tmp // 2 + 1, check)
    print(max(first, last, check))