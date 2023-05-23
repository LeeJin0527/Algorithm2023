import math
def solution(n):
    x = math.sqrt(n)
    if int(x)* int(x) == n:
        return int((x+1) * (x+1))
    else:
        return -1
