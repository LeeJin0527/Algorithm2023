def solution(array, commands):
    answer = []
    for command in commands:
        x, y, z = command
        check = array[x-1: y]
        check.sort()
        answer.append(check[z-1])
    return answer