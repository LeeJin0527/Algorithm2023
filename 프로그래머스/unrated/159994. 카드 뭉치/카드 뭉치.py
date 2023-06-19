from collections import defaultdict
def solution(cards1, cards2, goal):
    answer = ''
    check = defaultdict(int)
    for index, value in enumerate(cards1):
        check[value] = (index+1)
    for index, value in enumerate(cards2):
        check[value] = (index+1) + 100
    prev1 = -1
    prev2 = -1

    for value in goal:
        if 1 <= check[value] < 11:
            if prev1 == -1:
                prev1 = check[value]
            else:
                if check[value] != prev1 + 1:
                    return 'No'
                prev1 = check[value]
        elif 100 <= check[value] <= 111:
            if prev2 == -1:
                prev2 = check[value]
            else:
                if check[value] != prev2 + 1:
                    return 'No'
                prev2 = check[value]
            
    return 'Yes'