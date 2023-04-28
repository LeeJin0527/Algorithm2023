check = list(input().rstrip())
n = len(check)
num = check.count('a')
answer = int(1e9)
for index in range(n):
    if index + num <= n:
        sumOfIndexAndCountOfAIsUnderN = check[index: index + num]
        answer = min(answer, sumOfIndexAndCountOfAIsUnderN.count('b'))
    else:
        temp = num - len(check[index:])
        sumOfIndexAndCountOfAIsOverN = check[index:] + check[:temp]
        answer = min(answer, sumOfIndexAndCountOfAIsOverN.count('b'))
print(answer)