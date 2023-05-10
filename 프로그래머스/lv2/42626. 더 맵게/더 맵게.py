import heapq
def solution(scoville, K):
    def check(lst):
        for l in lst:
            if l < K:
                return False
        return True
    
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    while scoville:
        if len(scoville) <= 1:
            break
        if check(scoville):
            break
        answer += 1
        if len(scoville) >= 2:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x + (2*y))
    if check(scoville) == False:
        return -1
    return answer