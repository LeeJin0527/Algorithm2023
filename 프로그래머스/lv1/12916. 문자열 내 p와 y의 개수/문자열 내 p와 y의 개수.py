def solution(s):
    answer = True
    
    s = s.lower()

    x = s.count('p')
    y = s.count('y')
    if x == y:
        return True
    return False