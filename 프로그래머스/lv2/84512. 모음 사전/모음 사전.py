from itertools import product
def solution(word):
    answer = []
    check = ['A', 'E', 'I', 'O', 'U']
    for k in range(1, 6):
        for lst in list(product(check, repeat = k)):
            answer.append(''.join(lst))
    answer.sort()
    cnt = 1
    for ans in answer:
        if ans == word:
            return cnt
        cnt += 1
