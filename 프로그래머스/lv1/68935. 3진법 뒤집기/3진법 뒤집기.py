def solution(n):
    answer = 0
    baseThree = []
    while True:
        if n == 0:
            break
        baseThree.append(n % 3)
        n = n // 3
    baseThree = baseThree[::-1]

    for index, base in enumerate(baseThree):
        answer += base * (3**(index))
        
    return answer