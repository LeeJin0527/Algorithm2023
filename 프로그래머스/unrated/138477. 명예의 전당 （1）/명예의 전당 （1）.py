import copy
def solution(k, score):
    answer = []
    board = []
    for index, value in enumerate(score):
        if len(answer) == 0:
            answer.append(score[0])
            board.append(score[0])
            continue
        board.append(value)
        board.sort(reverse = True)
        if len(answer) + 1 >= k:
            board = board[:k]
        answer.append(board[-1])
    return answer