from collections import defaultdict
def solution(clothes):
    answer = 1
    clothDic = defaultdict(int)
    for cloth in clothes:
        name, status = cloth
        clothDic[status] += 1
    for cloth in clothDic:
        answer *= (clothDic[cloth] + 1)
    return answer - 1