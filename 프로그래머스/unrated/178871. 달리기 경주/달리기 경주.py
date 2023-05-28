from collections import defaultdict
def solution(players, callings):
    answer = []
    # 플레이어의 랭킹
    rank = defaultdict(int)
    # 플레이어의 위치
    location = defaultdict(int)
    for index, value in enumerate(players):
        rank[value] = index
        location[index] = value
 
    for index, value in enumerate(callings):
        backIndex = rank[value]
        frontIndex = backIndex - 1
        location[backIndex], location[frontIndex] = location[frontIndex] , location[backIndex]

        rank[location[backIndex]], rank[location[frontIndex]] = rank[location[frontIndex]], rank[location[backIndex]]
        
        
    for loc in location:
        answer.append(location[loc])
    return answer