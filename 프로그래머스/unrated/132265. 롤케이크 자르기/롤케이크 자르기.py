from collections import defaultdict
import copy
def solution(topping):
    answer = 0
    first = defaultdict(int)
    for top in topping:
        first[top] += 1
    second = defaultdict(int)
    
    for index in range(len(topping) -1, -1, -1):
        second[topping[index]] += 1
        first[topping[index]] -= 1
        if first[topping[index]] == 0:
            first.pop(topping[index])
        if len(first) == len(second):
            answer += 1
        
    return answer