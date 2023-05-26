def solution(citations):
    answer = 0
    for hIndex in range(max(citations), -1, -1):
        cnt = 0
        for citation in citations:
            if citation >= hIndex:
                cnt += 1
        if cnt >= hIndex:
            return hIndex
    return answer