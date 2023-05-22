def solution(t, p):
    answer = 0
    for index in range(len(t) - len(p) + 1):
        check = t[index: index+len(p)]
        if int(check) <= int(p):
            answer += 1
    return answer