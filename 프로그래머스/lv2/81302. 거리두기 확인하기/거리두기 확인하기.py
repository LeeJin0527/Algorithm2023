from itertools import combinations
def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for index, place in enumerate(places):
        flag = False
        for index in range(len(place)):
            place[index] = list(place[index])
        people = []
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    people.append([x, y])
        
        if len(people) == 0:
            answer.append(1)
            continue
        candidate = list(combinations(people, 2))

        for cand in candidate:
            a, b = cand[0]
            c, d = cand[1]
            if abs(a-c) + abs(b-d) <= 1:
                flag = True
                break
            elif abs(a-c) + abs(b-d) == 2:
                if (a == c) and (b != d):
                    ny = (b+d) // 2
                    if place[a][ny] != 'X':
                        flag = True
                        break
                if (b == d) and (a != c):
                    nx = (a+c) // 2
                    if place[nx][b] != 'X':
                        flag = True
                        break
                if (a != c) and (b != d):
                    if place[a][d] != 'X':
                        flag = True
                        break
                    if place[c][b] != 'X':
                        flag = True
                        break
                        
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer