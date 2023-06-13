from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    for index in range(len(discount)):
        flag = True
        temp = discount[index: index+10]
        check = defaultdict(int)
        for tem in temp:
            check[tem] += 1
        for idx, value in enumerate(want):
            if check[value] != number[idx]:
                flag = False
        if flag:
            answer += 1
    return answer