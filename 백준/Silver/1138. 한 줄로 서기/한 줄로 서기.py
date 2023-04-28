n = int(input())
people = list(map(int, input().split()))
check = [0] * n


for index, person in enumerate(people):
    move = -1
    for j in range(len(people)):
        if check[j] == 0:
            move += 1
        if move == person:
            check[j] = index + 1
            break
print(*check)