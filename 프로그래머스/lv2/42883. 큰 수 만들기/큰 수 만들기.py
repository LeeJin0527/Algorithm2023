def solution(number, k):
    answer = []
    number = list(map(int, number))
    for num in number:
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        answer.append(num)
    answer = list(map(str, answer))
    answer = str(int(''.join(answer)))[:len(number)-k]
    return answer