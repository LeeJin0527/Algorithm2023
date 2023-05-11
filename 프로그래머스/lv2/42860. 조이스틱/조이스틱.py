def solution(name):
    answer = 0
    for alpha in name:
        check = min(ord(alpha) - ord('A'), ord('Z') + 1 - ord(alpha))
        answer += check
    minValue = int(1e9)
    for index, value in enumerate(name):
        check = index + 1
        while check < len(name) and name[check] == 'A':
            check += 1
    
        first = index * 2 + len(name) - check 
        second = index + 2 * (len(name) - check)
        temp = min(first, second)
        minValue = min(temp, minValue)
    answer += minValue
    
    return answer