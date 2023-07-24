n = int(input())
s, g, p, d = map(int, input().split())
answer = 0
current = 0
check = list(input().rstrip())
temp = [0 for _ in range(len(check))]
for index, value in enumerate(check):
    if index == 0:
        if value == 'B':
            temp[index] = s - 1 # 29
        elif value == 'S':
            temp[index] = g-1 # 59
        elif value == 'G':
            temp[index] = p-1 # 89
        elif value == 'P':
            temp[index] = d-1 # 149
        elif value == 'D':
            temp[index] = d
    else:
        if value == 'B':
            temp[index] = (s-1) - temp[index-1]
        elif value == 'S':
            temp[index] = (g-1) - temp[index-1]
        elif value == 'G':
            temp[index] = (p-1) - temp[index-1]
        elif value == 'P':
            temp[index] = (d - 1) - temp[index - 1]
        elif value == 'D':
            temp[index] = d

print(sum(temp))
