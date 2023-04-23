menus = list(map(int, input().split()))
people = list(map(int, input().split()))
answer = 0
for index in range(3):
    if people[index] > menus[index]:
        answer += people[index] - menus[index]
print(answer)