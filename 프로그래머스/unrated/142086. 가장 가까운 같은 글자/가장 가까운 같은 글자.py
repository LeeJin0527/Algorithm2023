from collections import defaultdict
def solution(s):
    result = []
    checkCount = defaultdict(list)
    for index, value in enumerate(s):
        if len(checkCount[value]) < 1:
            result.append(-1)
        else:
            result.append(index - checkCount[value][-1])
        checkCount[value].append(index)
            
    return result