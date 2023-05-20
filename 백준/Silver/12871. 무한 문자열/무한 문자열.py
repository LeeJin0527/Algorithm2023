x = input().rstrip()
y = input().rstrip()
check = len(x) * len(y)
x = list(x)
y = list(y)
first, second = [], []
for index in range(check):
    first.append(x[index % len(x)])
    second.append(y[index % len(y)])

if first == second:
    print(1)
else:
    print(0)