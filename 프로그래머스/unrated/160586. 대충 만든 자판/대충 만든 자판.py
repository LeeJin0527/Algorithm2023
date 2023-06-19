def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for targetValue in target:
            check = int(1e9)
            for key in keymap:
                for index, value in enumerate(key):
                    if value == targetValue:
                        check = min(check, index+1)
                        break
            result += check
        if result >= int(1e9):
            answer.append(-1)
        else:
            answer.append(result)
                
    return answer