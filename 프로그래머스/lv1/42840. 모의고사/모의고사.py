def solution(answers):
    answer = []
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    maxValue = 0
    for k in range(3):
        cnt = 0
        for index, value in enumerate(answers):
            if value == students[k][index % len(students[k])]:
                cnt += 1
        if cnt >= maxValue:
            if cnt > maxValue:
                answer = []
            maxValue = cnt
            answer.append(k+1)
    return answer