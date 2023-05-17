def solution(name, yearning, photo):
    answer = []
    checkName = dict()
    for index, value in enumerate(name):
        checkName[value] = yearning[index]

    for index, value in enumerate(photo):
        result = 0
        for person in value:
            if person in name:
                result += checkName[person]
        answer.append(result)
        
    return answer