from collections import deque
def solution(priorities, location):
    answer = []
    valueDeque = deque()
    totalDeque = deque()
    for index, value in enumerate(priorities):
        valueDeque.append(value)
        totalDeque.append([value, index])
    print(valueDeque)
    print(totalDeque)
    
    while totalDeque:
        if len(totalDeque) == 1:
            value, index = totalDeque.popleft()
            answer.append([value, index])
            break
        value, index = totalDeque.popleft()
        checkValue = valueDeque.popleft()
        if value >= max(valueDeque):
            answer.append([value, index])
        else:
            totalDeque.append([value, index])
            valueDeque.append(checkValue)
    for index, value in enumerate(answer):
        if value[1] == location:
            return index + 1
