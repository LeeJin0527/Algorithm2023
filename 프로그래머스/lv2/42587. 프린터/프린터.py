from collections import deque
def solution(priorities, location):
    answer = []
    q = deque()
    for index, value in enumerate(priorities):
        q.append([value, index])
    while q:
        temp = []
        if len(q) == 1:
            value, index = q.popleft()
            answer.append([value, index])
            break
        value, index = q.popleft()
        for each in q:
            temp.append(each[0])
        if value >= max(temp):
            answer.append([value, index])
        else:
            q.append([value, index])
    for index, value in enumerate(answer):
        if value[1] == location:
            return index + 1