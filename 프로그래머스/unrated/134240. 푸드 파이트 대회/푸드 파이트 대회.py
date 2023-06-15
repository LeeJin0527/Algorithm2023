def solution(food):
    answer = ''
    for index in range(1, len(food)):
        answer += str(index) * (food[index] // 2)
    right = answer[::-1]
    answer += '0'
    answer += right
    return answer