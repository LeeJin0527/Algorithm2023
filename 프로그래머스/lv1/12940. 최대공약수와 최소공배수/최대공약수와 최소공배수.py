import math
def solution(n, m):
    answer = []
    x = math.gcd(n, m)
    y = (n*m) // x
    answer = [x, y]
    return answer