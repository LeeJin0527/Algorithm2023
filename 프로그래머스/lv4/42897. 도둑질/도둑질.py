def solution(money):
    answer = 0
    first = [0] + money[1:]
    second = [0] + money[:-1]
    
    firstDP = [0] * len(money)
    secondDP = [0] * len(money)
    
    firstDP[0] = first[0]
    firstDP[1] = max(first[0], first[1])
    
    secondDP[0] = second[0]
    secondDP[1] = max(second[0], second[1])
    
    for index in range(2, len(first)):
        firstDP[index] = max(firstDP[index-1], firstDP[index-2] + first[index])
        secondDP[index] = max(secondDP[index-1], secondDP[index-2] + second[index])
    
    
    return max(firstDP[-1], secondDP[-1])