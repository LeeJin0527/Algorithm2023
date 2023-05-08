import sys
input = sys.stdin.readline

while True:
    temp = input().rstrip()
    board = [[] for _ in range(3)]
    if temp == 'end':
        break
    temp = list(temp)
    for index, tem in enumerate(temp):
        board[index // 3].append(tem)
    check = [[(0, 0), [(0, 2), (2, 2), (2, 0)]],
             [(0, 1), [(2, 1)]],
             [(0, 2), [(2, 0), (2, 2)]],
             [(1, 0), [(1, 2)]],
             [(2, 0), [(2, 2)]]]
    xCount = 0
    yCount = 0
    for che in check:
        start_x, start_y = che[0]
        for each in che[1]:
            end_x, end_y = each
            if start_x != end_x and start_y == end_y:
                checkCount = 0
                for i in range(3):
                    if board[start_x][start_y] == board[start_x + i][end_y]:
                        checkCount += 1
                if checkCount == 3:
                    if board[start_x][start_y] == 'X':
                        xCount += 1
                    elif board[start_x][start_y] == 'O':
                        yCount += 1
            elif start_x == end_x and start_y != end_y:
                checkCount = 0
                for i in range(3):
                    if board[start_x][start_y] == board[end_x][start_y + i]:
                        checkCount += 1
                if checkCount == 3:
                    if board[start_x][start_y] == 'X':
                        xCount += 1
                    elif board[start_x][start_y] == 'O':
                        yCount += 1

            elif start_x != end_x and start_y != end_y:
                if start_x == 0 and start_y == 2 and end_x == 2:
                    checkCount = 0
                    for i in range(3):
                        if board[start_x][start_y] == board[start_x + i][start_y - i]:
                            checkCount += 1
                    if checkCount == 3:
                        if board[start_x][start_y] == 'X':
                            xCount += 1
                        elif board[start_x][start_y] == 'O':
                            yCount += 1

                else:
                    checkCount = 0
                    for i in range(3):
                        if board[start_x][start_y] == board[start_x + i][start_y + i]:
                            checkCount += 1
                    if checkCount == 3:
                        if board[start_x][start_y] == 'X':
                            xCount += 1
                        elif board[start_x][start_y] == 'O':
                            yCount += 1
    if xCount > 0:
        if yCount >= 1:
            print("invalid")
            continue
        else:
            if temp.count('X') == temp.count('O') + 1:
                print("valid")
                continue
    elif yCount > 0:
        if temp.count('X') == temp.count('O'):
            print("valid")
            continue
    elif temp.count('X') == 5 and temp.count('O') == 4:
        print("valid")
        continue
    elif xCount >= 1 and yCount >= 1:
        print("invalid")
        continue
    print("invalid")
