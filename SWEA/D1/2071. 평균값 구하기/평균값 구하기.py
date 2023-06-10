t = int(input())
for n in range(1, t+1):
    numbers = list(map(int, input().split()))
    print(f'#{n} {round(sum(numbers) / 10)}')
