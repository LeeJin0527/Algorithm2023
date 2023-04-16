def solution(array, commands):
    answer = []
    for command in commands:
        x, y, check = command
        temp = array[x-1: y]
        temp.sort()
        answer.append(temp[check-1])
    return answer