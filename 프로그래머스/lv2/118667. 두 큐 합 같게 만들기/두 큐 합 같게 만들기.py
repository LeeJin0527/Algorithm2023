def solution(queue1, queue2):
    answer = 0
    newQueue = queue1 + queue2
    start, end = -1, len(queue1) -1
    if sum(newQueue) % 2 == 1:
        return -1
    target = sum(newQueue) // 2
    
    check = sum(newQueue[start + 1 : end+1])

    while True:
        if check < target and end == len(newQueue)-1:
            return -1
        if check == target:
            return answer
        if start == len(newQueue) -1:
            break

        if check < target and end < len(newQueue) - 1:
            end += 1
            check += newQueue[end]
            answer += 1
        elif check > target and start < end:
            start += 1
            check -= newQueue[start]
            answer += 1
            
    if sum(newQueue[:start]) != sum(newQueue[end:]):
        return -1

    if start == end:
        return -1
            
    return answer