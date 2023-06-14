def check(num, length):
    answer = []
    while True:
        if num == 0:
            break
        answer.append(num % 2)
        num = num // 2
        
    answer = answer[::-1]
    if len(answer) < length:
        k = length - len(answer)
        answer = [0 for _ in range(k)] + answer
    return answer
        
        
def solution(n, arr1, arr2):
    answer = [[-1 for _ in range(n)] for _ in range(n)]
    for index, arr in enumerate(arr1):
        res = check(arr, n)
        answer[index] = res
    for index, arr in enumerate(arr2):
        res = check(arr, n)
        for x in range(len(res)):
            answer[index][x] = (res[x] | answer[index][x])
    for x in range(n):
        for y in range(n):
            if answer[x][y] == 1:
                answer[x][y] = '#'
            else:
                answer[x][y] = ' '
    for index, value in enumerate(answer):
        answer[index] = ''.join(value)
    return answer