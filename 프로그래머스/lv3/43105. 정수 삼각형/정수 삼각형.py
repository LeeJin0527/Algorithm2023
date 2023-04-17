def solution(triangle):
    for index, value in enumerate(triangle):
        triangle[index] = [0] + triangle[index] + [0]
    
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    return answer