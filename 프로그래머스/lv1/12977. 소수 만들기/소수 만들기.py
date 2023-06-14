from itertools import combinations
import math
def primeNum(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    lst = list(combinations(nums, 3))
    for l in lst:
        if primeNum(sum(l)):
            answer += 1
    return answer