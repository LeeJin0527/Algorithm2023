from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []
    genresCount = defaultdict(int)
    playsCount = defaultdict(list)
    for index, genre in enumerate(genres):
        genresCount[genre] += plays[index]   
    genresCount = sorted(genresCount.items(), key= operator.itemgetter(1), reverse = True)
    
    for index, genre in enumerate(genres):
        playsCount[genre].append([plays[index], index])
        
        
    for genre in genresCount:
        temp = sorted(playsCount[genre[0]], key=lambda x: (-x[0], x[1]))
        if len(temp) >= 2:
            answer.append(temp[0][1])
            answer.append(temp[1][1])
        else:
            for index in range(len(temp)):
                answer.append(temp[index][1])
    
    return answer