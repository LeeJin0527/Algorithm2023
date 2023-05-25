import math
def prime_number(num):
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True
            
    
    
def solution(n):
    answer = 0
    for x in range(2, n+1):
        if prime_number(x):
            answer += 1
    return answer