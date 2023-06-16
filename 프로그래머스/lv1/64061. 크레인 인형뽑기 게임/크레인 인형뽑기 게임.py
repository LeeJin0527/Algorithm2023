def solution(board, moves):
    answer = 0
    store = []
    for move in moves:
        while len(store) >= 2 and store[-1] == store[-2]:
            answer += 2
            store = store[:-2]
            print(store)
        tmp = []
        check = -1
        for x in range(len(board)):
            tmp.append(board[x][move-1])
        if tmp.count(0) == len(board):
            continue
        for index, each in enumerate(tmp):
            if each > 0:
                check = each
                board[index][move-1] = 0
                break
        store.append(check)
    return answer