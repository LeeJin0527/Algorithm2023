import heapq
def solution(operations):
    answer = []
    for operation in operations:
        x, y = operation.split()
        if x == 'I':
            heapq.heappush(answer, int(y))
        elif x == 'D':
            if len(answer) == 0:
                continue
            if int(y) == 1:
                answer = heapq.nlargest(len(answer), answer)[1:]
                heapq.heapify(answer)
            elif int(y) == -1:
                heapq.heappop(answer)
    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]