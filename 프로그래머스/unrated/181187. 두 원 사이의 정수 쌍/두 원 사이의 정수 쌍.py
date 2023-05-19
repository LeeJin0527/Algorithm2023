import math
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        max_y = math.sqrt((r2*r2) - (x*x))
        min_y = 0 if x > r1 else math.sqrt((r1*r1) - (x*x))
        answer += math.floor(max_y) - math.ceil(min_y) + 1
    return answer * 4