def solution(ingredient):
    index = 0
    answer = 0
    while True:

        if len(ingredient) < 4 or index == len(ingredient) - 3:
            break
        if ingredient[index:index+4] == [1, 2, 3, 1]:
            del ingredient[index:index+4]
            answer += 1
            index -= 3
        index += 1
        
    return answer