def solution(s):
    answer = ''
    small, big = [], []
    for each in s:
        if 65 <= ord(each) <= 90:
            big.append(each)
        elif 97 <= ord(each) <= 122:
            small.append(each)
    small.sort(reverse = True)
    big.sort(reverse = True)
    for s in small:
        answer += s
    for b in big:
        answer += b
    return answer