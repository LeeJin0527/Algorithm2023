def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        check = 0
        for time in times:
            check += mid // time
        if check >= n:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
    return answer