def solution(n, m, section):
    now, answer = section[0] - 1, 0
    
    for sec in section:
        if now < sec:
            now = sec + m - 1
            answer += 1
    return answer