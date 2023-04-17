def solution(array):
    answer = -1
    for index, value in enumerate(array):
        if index % 2 == 0:
            array[index] = int(value)
    n = len(array)
    minDp = [[0 for _ in range(n)] for _ in range(n)]
    maxDp = [[0 for _ in range(n)] for _ in range(n)]
    
    for index in range(0, n, 2):
        maxDp[index][index] = array[index]
        minDp[index][index] = array[index]

    for x in range(3, n+1, 2):
        for start in range(0, n-1, 2):
            # end - start +1 = x
            end = x + start - 1
            if end >= n:
                break
            maxTemp = []
            minTemp = []
            
            for operation in range(start+1, end, 2):
                if array[operation] == '+':
                    maxTemp.append(maxDp[start][operation-1] + maxDp[operation+1][end])
                    minTemp.append(minDp[start][operation-1] + minDp[operation+1][end])
                elif array[operation] == '-':
                    maxTemp.append(maxDp[start][operation-1] - minDp[operation+1][end])
                    minTemp.append(minDp[start][operation-1] - maxDp[operation+1][end])
            maxDp[start][end] = max(maxTemp)
            minDp[start][end] = min(minTemp)
    answer = maxDp[0][-1]  
    return answer