def solution(elements):
    answer = set()
    n = len(elements)
    newElements = elements * 1000

    for index in range(1, n+1):
        for j in range(n):
            answer.add(sum(newElements[j : (j + index)]))

    return len(answer)