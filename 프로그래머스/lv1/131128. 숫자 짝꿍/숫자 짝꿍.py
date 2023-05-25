from collections import Counter
def solution(X, Y):
    answer = ''
    check = []
    compareX = Counter(X)
    compareY = Counter(Y)

    for compare in compareX:
        if compare in compareY:
            temp = min(compareX[compare], compareY[compare])
            check.extend(list(temp * compare))

    if len(check) == 0:
        return "-1"
    check.sort(reverse = True)
    if check[0] == '0':
        return "0"
    return ''.join(check)