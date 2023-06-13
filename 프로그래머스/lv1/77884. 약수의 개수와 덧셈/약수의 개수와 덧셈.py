def check(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    if cnt % 2 == 0:
        return True
    return False

def solution(left, right):
    answer = 0
    for value in range(left, right+1):
        if check(value):
            answer += value
        else:
            answer -= value
    return answer