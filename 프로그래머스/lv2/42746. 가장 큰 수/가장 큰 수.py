def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)* 3, reverse = True)
    numbers = list(map(str, numbers))
    return str(int(''.join(numbers)))