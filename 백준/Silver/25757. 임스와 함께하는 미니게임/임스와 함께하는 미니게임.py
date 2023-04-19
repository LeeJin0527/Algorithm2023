n, game = input().split()
n = int(n)
check = set()
for _ in range(n):
    check.add(input().rstrip())
if game == 'Y':
    print(len(check))
elif game == 'F':
    print(len(check) // 2)
elif game == 'O':
    print(len(check) // 3)