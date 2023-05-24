def solution(s):
    answer = True
    if len(s) != 4 and (len(s) != 6):
        return False
    cnt = 0
    for each in s:
        if 48 <= ord(each) <= 57:
            cnt += 1
    if cnt == len(s):
        return True
    return False