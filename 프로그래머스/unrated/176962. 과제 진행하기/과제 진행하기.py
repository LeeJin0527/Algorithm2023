def solution(plans):
    answer, check, stack = [], [], []
    plans.sort(key=lambda x: x[1])
    for plan in plans:
        subject, start, duration = plan
        hour, minute = start.split(":")
        check.append([subject, 60 * int(hour) + int(minute), int(duration)])
    leftTime = 0
    for i in range(len(check)):
        subject, start, duration = check[i]
        while stack:
            prevSubject, prevDuration = stack.pop()
            if leftTime >= prevDuration:
                leftTime -= prevDuration
                answer.append(prevSubject)
            else:
                stack.append([prevSubject, prevDuration - leftTime])
                break
        stack.append([subject, duration])
        if i < len(check)-1:
            nextStart = check[i+1][1]
            leftTime = nextStart - start
    
    while stack:
        ans, _ = stack.pop()
        answer.append(ans)
    return answer