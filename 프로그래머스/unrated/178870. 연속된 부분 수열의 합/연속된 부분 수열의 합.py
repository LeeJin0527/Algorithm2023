def solution(sequence, k):
    answer = []
    start, end = 0, 0
    n = len(sequence)
    sumNum = 0
    while start < n:
        
        while end < n and sumNum < k:
            sumNum += sequence[end]
            end += 1
        if sumNum == k:
            if start == end:
                answer.append([start, end])
            else:
                answer.append([start, end-1])
        sumNum -= sequence[start]
        start += 1
    answer.sort(key=lambda x: ((x[1] - x[0]), x[0]))
    return answer[0]