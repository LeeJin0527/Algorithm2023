def solution(citations):
    start = max(citations)
    for index in range(start, -1, -1):
        cnt = 0
        for citation in citations:
            if citation >= index:
                cnt += 1
        if cnt >= index:
            return index