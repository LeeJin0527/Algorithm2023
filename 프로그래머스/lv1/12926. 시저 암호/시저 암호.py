def solution(s, n):
    answer = ''
    for value in s:
        if value == ' ':
            answer += value
            continue
        if 65 <= ord(value) <= 90:
            if (ord(value) + n) > 90:
                answer += chr((ord(value) + n) - 26)
            else:
                answer += chr((ord(value) + n))
        elif 97 <= ord(value) <= 122:
            if (ord(value) + n) > 122:
                answer += chr((ord(value) + n) - 26)
            else:
                answer += chr((ord(value) + n))
        
    return answer