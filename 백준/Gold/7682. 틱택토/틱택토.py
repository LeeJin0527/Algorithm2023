import sys
input = sys.stdin.readline
check = [[(0, 0), [(0, 2), (2, 2), (2, 0) ]],
         [(0, 1), [(2, 1)]],
         [(0, 2), [(2, 0), (2, 2)]],
         [(1, 0), [(1, 2)]],
         [(2, 0), [(2, 2)]]]

def xoCount(check, pan):
    xCnt, oCnt = 0, 0
    for che in check:
        start_x, start_y = che[0]
        for each in che[1]:
            end_x, end_y = each
            if start_x == 0 and start_y == 2 and end_x == 2 and end_y == 0:
                count = 0
                for i in range(3):
                    if pan[start_x][start_y] == pan[start_x + i][start_y - i]:
                        count += 1
                if count == 3:
                    if pan[start_x][start_y] == 'X':
                        xCnt += 1
                    elif pan[start_x][start_y] == 'O':
                        oCnt += 1

            elif start_x < end_x:
                if start_y < end_y:
                    count = 0
                    for i in range(3):
                        if pan[start_x][start_y] == pan[start_x + i][start_y + i]:
                            count += 1
                    if count == 3:
                        if pan[start_x][start_y] == 'X':
                            xCnt += 1
                        elif pan[start_x][start_y] == 'O':
                            oCnt += 1
                elif start_y == end_y:
                    count = 0
                    for i in range(3):
                        if pan[start_x][start_y] == pan[start_x + i][start_y]:
                            count += 1
                    if count == 3:
                        if pan[start_x][start_y] == 'X':
                            xCnt += 1
                        elif pan[start_x][start_y] == 'O':
                            oCnt += 1
            elif start_x == end_x:
                if start_y < end_y:
                    count = 0
                    for i in range(3):
                        if pan[start_x][start_y] == pan[start_x][start_y + i]:
                            count += 1
                    if count == 3:
                        if pan[start_x][start_y] == 'X':
                            xCnt += 1
                        elif pan[start_x][start_y] == 'O':
                            oCnt += 1
    return xCnt, oCnt
while True:
    origin = input().rstrip()
    if origin == 'end':
        break
    board = [[] for _ in range(3)]
    for index, value in enumerate(origin):
        board[index // 3].append(value)
    ## X O 몇 빙고 나오는지 세기
    xCount, oCount = xoCount(check, board)
    # print(xCount, oCount)
    ## 빙고 종료 조건
    # X 승리
    if xCount > 0:
        if oCount > 0:
            print("invalid")
            continue
        else:
            if origin.count('X') == origin.count('O') + 1:
                print("valid")
                continue
    # Y 승리
    elif oCount > 0:
        if origin.count('X') == origin.count('O'):
            print("valid")
            continue
    # 무승부
    elif origin.count('X') == 5 and origin.count('O') == 4:
        print("valid")
        continue
    print("invalid")
