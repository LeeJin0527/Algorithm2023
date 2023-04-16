import heapq
def check(lst, target):
    for l in lst:
        if l < target:
            return False
    return True

def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    cnt = 0
    while scoville:
        if check(scoville, K) :
                return cnt
        if len(scoville) == 1:
            if check(scoville, K) :
                return cnt
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2* second)
        cnt += 1
    return -1