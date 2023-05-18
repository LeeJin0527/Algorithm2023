def solution(n):
    answer = 0
    check = list(str(n))
    check.sort(reverse = True)

    return int(''.join(check))