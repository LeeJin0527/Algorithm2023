def solution(citations):
    answer = 0
    candidate = max(citations)
    for index in range(candidate, -1, -1):
        temp = 0
        for citation in citations:
            if citation >= index:
                temp += 1
        if temp >= index:
            return index