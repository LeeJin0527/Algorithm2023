import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    start, now, cnt = -1, 0, 0
    q = []
    while True:
        if cnt == len(jobs):
            break
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, [job[1], job[0]])
        if q:
            x, y = heapq.heappop(q)
            start = now
            now += x
            answer += now - y
            cnt += 1
        else:
            now += 1

    return answer // len(jobs)