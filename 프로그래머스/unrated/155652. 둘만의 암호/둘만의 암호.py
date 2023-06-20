def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    for each in s:
        cnt = 0
        idx = 1
        while True:
            check = chr(ord(each) + idx)
            
            if ord(check) > 122:
                temp = ord(check) % 123
                temp = temp % 26
                check = chr(temp + 97)
            if check not in skip:
                cnt += 1
            idx += 1
            if cnt == index:
                break
        if ord(check) > 122:
            temp = ord(check) % 123
            check = chr(temp + 97)
        answer += check
    return answer