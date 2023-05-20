t = int(input())
for number in range(1, t+1):
    n = int(input())
    if n % 2 != 0:
        answer = 'Odd'
    else:
        answer = 'Even'
    print(f'#{number} {answer}')