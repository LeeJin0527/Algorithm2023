n = int(input())
cookies = []
for _ in range(n):
    cookies.append(list(input().rstrip()))
flag = False
heart = []
for index, value in enumerate(cookies):
    if flag:
        break
    if '*' in value:
        for j in range(len(cookies[index])):
            if cookies[index][j] == '*':
                flag = True
                heart = [index + 2, j+1]
                break
print(*heart)
left, right, waist, leftLeg, rightLeg = 0, 0, 0, 0, 0

for j in range(0, heart[1]-1):
    if cookies[heart[0]-1][j] == '*':
        left += 1
for j in range(heart[1], n):
    if cookies[heart[0]-1][j] == '*':
        right += 1

for j in range(heart[0], n):
    if cookies[j][heart[1]-1] == '*':
        waist += 1

for j in range(heart[0], n):
    if cookies[j][heart[1]-2] == '*':
        leftLeg += 1
for j in range(heart[0], n):
    if cookies[j][heart[1]] == '*':
        rightLeg += 1
print(left, right, waist, leftLeg, rightLeg)