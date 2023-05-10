from itertools import permutations
import math
def is_prime(number):
    for index in range(2, int(math.sqrt(number)) + 1 ):
        if number % index == 0:
            return False
    return True
    
    
def solution(numbers):
    check = set()
    numbers = list(map(int, numbers))
    for k in range(1, len(numbers)+1):
        for lst in list(permutations(numbers, k)):
            lst = list(map(str, lst))
            temp = int(''.join(lst))
            if temp not in check and is_prime(temp) and temp != 0 and temp != 1:
                check.add(temp)
    return len(check)