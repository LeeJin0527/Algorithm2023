from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []
    countGenres = defaultdict(int)
    music = defaultdict(list)
    for index, value in enumerate(genres):
        countGenres[value] += plays[index]
        music[value].append([plays[index], index])

    countGenres = sorted(countGenres.items(), key=operator.itemgetter(1), reverse = True)
    for count in countGenres:
        check = sorted(music[count[0]], key=lambda x: (-x[0], x[1]))
        if len(check) >= 2:
            answer.append(check[0][1])
            answer.append(check[1][1])
        else:
            for k in range(len(check)):
                answer.append(check[k][1])
        
    return answer