import math
t = int(input())
def is_prime(num):
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

for number in range(1, t+1):
    n = int(input())
    check = 1
    while True:
        if not is_prime(check) and not is_prime(check + n):
            print(f'#{number} {check+n} {check}')
            break
        check += 1
