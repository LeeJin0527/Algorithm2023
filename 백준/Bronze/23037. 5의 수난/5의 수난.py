numbers = list(map(int, input().rstrip()))
answer = 0
for num in numbers:
    answer += num ** 5
print(answer)