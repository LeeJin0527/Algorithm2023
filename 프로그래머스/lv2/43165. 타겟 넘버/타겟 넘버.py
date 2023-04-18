def dfs(res, cnt, end, target, numbers):
    global answer
    if cnt == end:
        if res == target:
            answer += 1
        return 
    
    dfs(res + numbers[cnt], cnt + 1, end, target, numbers)
    dfs(res - numbers[cnt], cnt + 1, end, target, numbers)

def solution(numbers, target):
    dfs(0, 0, len(numbers), target, numbers)
    return answer
answer = 0