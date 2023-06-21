import math
def check(num):
    cnt = 0
    for i in range(1,  int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 2
            if num // i == i:
                cnt -= 1
    return cnt

def solution(number, limit, power):
    answer = 0
    result = []
    for index in range(1, number+1):
        res = check(index)
        result.append(res)

    for res in result:
        if res > limit:
            answer += power
        else:
            answer += res
    return answer