import heapq
def solution(operations):
    answer = []
    for operation in operations:
        operation = list(operation.split())
        if operation[0] == 'I':
            heapq.heappush(answer, int(operation[1]))
        elif operation[0] == 'D':
            if len(answer) == 0:
                continue
            if operation[1] == '1':
                answer = heapq.nlargest(len(answer), answer)[1:]
                heapq.heapify(answer)
            elif operation[1] == '-1':
                heapq.heappop(answer)

    if len(answer) == 0:
        return [0, 0]
    else:
        return [int(max(answer)), int(min(answer))]
    return answer