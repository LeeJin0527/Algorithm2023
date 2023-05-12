import copy
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2
        pre, cnt = 0, 0
        for index, value in enumerate(rocks):
            if value - pre < mid:
                cnt += 1
            else:
                pre = value
            if cnt > n:
                break
        if cnt > n:
            end = mid -1
        else:
            answer = mid
            start = mid + 1
            
    return answer