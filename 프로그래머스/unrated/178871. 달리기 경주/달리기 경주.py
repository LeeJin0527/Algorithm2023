from collections import defaultdict
def solution(players, callings):
    answer = []
    rank = defaultdict(int)
    location = defaultdict(int)
    for index, value in enumerate(players):
        rank[value] = index
        location[index] = value
    
    for index, value in enumerate(callings):
        curIndex = rank[value]
        preIndex = curIndex -1
        location[curIndex], location[preIndex] = location[preIndex], location[curIndex]
        rank[location[curIndex]], rank[location[preIndex]] = rank[location[preIndex]], rank[location[curIndex]]
    for loc in location:
        answer.append(location[loc])
    return answer