def solution(x):
    check = list(map(int, str(x)))
    if x % sum(check) == 0:
        return True
    return False