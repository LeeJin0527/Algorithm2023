def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance
    while start <= end:
        mid = (start+ end) // 2
        pre_rock, cnt = 0, 0
        for rock in rocks:
            if rock - pre_rock < mid:
                cnt += 1
            else:
                pre_rock = rock
            if cnt > n:
                break
        if cnt > n:
            end = mid -1
        else:
            answer = mid
            start = mid + 1
    return answer