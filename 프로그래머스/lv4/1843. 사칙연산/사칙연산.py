def solution(arr):
    answer = -1
    n = len(arr)
    max_dp = [[0 for _ in range(n)] for _ in range(n)]
    min_dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for index in range(0, len(arr), 2):
        arr[index] = int(arr[index])
        max_dp[index][index] = int(arr[index])
        min_dp[index][index] = int(arr[index])
    
    for index in range(3, len(arr)+1, 2):
        for left in range(0, len(arr), 2):
            right = index + left - 1
            if right >= len(arr):
                break
            print(left, right)
            checkMinValue = []
            checkMaxValue = []
            for operator in range(left+1, right, 2):
                if operator >= len(arr):
                    break
                if arr[operator] == '-':
                    checkMaxValue.append(max_dp[left][operator-1] - min_dp[operator+1][right])
                    checkMinValue.append(min_dp[left][operator-1] - max_dp[operator+1][right])
                elif arr[operator] == '+':
                    checkMaxValue.append(max_dp[left][operator-1] + max_dp[operator+1][right])
                    checkMinValue.append(min_dp[left][operator-1] + min_dp[operator+1][right])
            max_dp[left][right] = max(checkMaxValue)
            min_dp[left][right] = min(checkMinValue)
    return max_dp[0][-1]