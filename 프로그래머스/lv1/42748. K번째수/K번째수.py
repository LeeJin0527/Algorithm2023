def solution(array, commands):
    answer = []
    for command in commands:
        start, end, num = command
        check = array[start-1: end]
        check.sort()
        answer.append(check[num-1])
    return answer