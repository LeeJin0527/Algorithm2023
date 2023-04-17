def solution(name):
    answer = 0
    min_value = int(1e9)
    for index, value in enumerate(name):
        first = ord('Z') - ord(value) + 1
        second = ord(value) - ord('A')
        answer += min(first, second)
        next = index + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_value = min(min_value, index*2 + (len(name) - next), index + 2*(len(name) - next))
    answer += min_value
    return answer