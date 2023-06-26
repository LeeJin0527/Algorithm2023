from collections import deque
def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x: x[1])
    check = []
    for plan in plans:
        subject, start, duration = plan
        hour, minute = start.split(":")
        total = 60 * int(hour) + int(minute)
        check.append([subject, total, int(duration)])
    
    for i in range(len(check)):
        subject, start, duration = check[i]
        while stack:
            prevSubject, prevTime = stack.pop()
            if leftTime >= prevTime:
                leftTime -= prevTime
                answer.append(prevSubject)
            else:
                stack.append([prevSubject, prevTime - leftTime])
                break
            
            
        stack.append([subject, duration])
        if i < len(check)-1:
            nextStart = check[i+1][1]
            leftTime = nextStart - start
    while stack:
        ans, _ = stack.pop()
        answer.append(ans)
    return answer 