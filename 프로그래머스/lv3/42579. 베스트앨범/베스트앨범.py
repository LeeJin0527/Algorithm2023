from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []
    countDic = defaultdict(int)
    genreDic = defaultdict(list)
    for index, value in enumerate(genres):
        countDic[value] += plays[index]
        genreDic[value].append([plays[index], index])
    
    count = sorted(countDic.items(), key=operator.itemgetter(1), reverse = True)
    for genre in genreDic:
        genreDic[genre].sort(key=lambda x: [-x[0], x[1]])
    
    for cou in count:
        tempCnt = 0
        for i in range(len(genreDic[cou[0]])):
            if tempCnt >= 2:
                break
            answer.append(genreDic[cou[0]][i][1])
            tempCnt += 1
            
    return answer