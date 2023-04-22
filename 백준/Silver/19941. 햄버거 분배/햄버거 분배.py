import sys
input = sys.stdin.readline
n, k = map(int, input().split())
desk = list(input().rstrip())
person, hambuger = [], []
for index, value in enumerate(desk):
    if value == 'P':
        person.append(index)
    elif value == 'H':
        hambuger.append(index)

origin = len(hambuger)
check = []
for index, value in enumerate(person):
    for each in range(value-k, value + k+1):
        if each in hambuger:
            hambuger.remove(each)
            break
print(origin - len(hambuger))