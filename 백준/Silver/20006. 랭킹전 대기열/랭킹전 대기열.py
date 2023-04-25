p, m = map(int, input().split())
rooms, check = [[] for _ in range(501)], []
for _ in range(p):
    level, name = input().rstrip().split()
    check.append([int(level), name])
rooms = []
for level, name in check:
    flag = True
    for index in range(len(rooms)):
        if len(rooms[index][1]) == m:
            continue
        if rooms[index][0] - 10 <= level <= rooms[index][0] + 10:
            flag = False
            rooms[index][1].append([level, name])
            break
    if flag:
        rooms.append([level, [[level, name]]])

for room in rooms:
    x, room = room
    room.sort(key=lambda x:x[1])
    if len(room) == m:
        print('Started!')
        for each in room:
            print(*each)

    else:
        print('Waiting!')
        for each in room:
            print(*each)
