def solution(price, money, count):
    answer = 0
    for index in range(1, count+1):
        answer += price * index
    if answer - money < 0:
        return 0
    return answer - money