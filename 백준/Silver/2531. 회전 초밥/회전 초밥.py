n, d, k, c = map(int, input().split())
dishes = []
for _ in range(n):
    dishes.append(int(input()))
answer = 0
for index in range(n):
    if index + k < n:
        check = dishes[index: index+k]
        if c in set(check):
            answer = max(answer, len(set(check)))
        else:
            answer = max(answer, len(set(check)) + 1)
    else:
        temp = k - len(dishes[index:])
        check = dishes[index:] + dishes[:temp]
        if c in set(check):
            answer = max(answer, len(set(check)))
        else:
            answer = max(answer, len(set(check)) + 1)
print(answer)