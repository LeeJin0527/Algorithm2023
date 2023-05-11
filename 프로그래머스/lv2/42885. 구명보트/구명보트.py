from collections import deque
def solution(people, limit):
    answer = 0
    if len(people) == 1:
        return 1
    people.sort(reverse = True)
    people = deque(people)
    
    while people:
        if len(people) > 2:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                answer += 1
            else:
                people.popleft()
                answer += 1
        else:
            if people[0] + people[-1] <= limit and len(people) == 2:
                people.popleft()
                people.pop()
                answer += 1
            else:
                answer += len(people)
                break
    return answer