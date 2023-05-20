t = int(input())
for number in range(1, t+1):
    x, y = input().rstrip().split()
    check = len(x) * len(y)
    x = list(x)
    y = list(y)
    first, second = [], []
    for index in range(check):
        first.append(x[index % len(x)])
        second.append(y[index % len(y)])

    if first == second:
        print(f'#{number} yes')
    else:
        print(f'#{number} no')

