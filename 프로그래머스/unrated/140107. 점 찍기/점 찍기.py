import math
def solution(k, d):
    x = 0
    answer = 0
    while True:
        if d ** 2 - x ** 2 < 0:
            break
        check = int(math.sqrt(d ** 2 - x ** 2))
        answer += check // k + 1
        x += k
    return answer