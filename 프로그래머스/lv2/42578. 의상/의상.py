from collections import defaultdict
def solution(clothes):
    answer = 1
    check = defaultdict(int)
    for cloth in clothes:
        name, status = cloth
        check[status] += 1
    for che in check:
        answer *= (check[che] + 1)
    return answer - 1