def solution(numbers, target):
    
    def dfs(res, cnt):
        global answer
        if cnt == len(numbers):
            if res == target:
                answer += 1
            return 
        dfs(res + numbers[cnt], cnt + 1)
        dfs(res - numbers[cnt], cnt + 1)
    
    dfs(0, 0)
    return answer
answer = 0