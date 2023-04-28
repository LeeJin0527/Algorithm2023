p, m = map(int, input().split())
rooms = []
for _ in range(p):
    level, name = input().rstrip().split()
    level = int(level)
    flag = True

    for index, room in enumerate(rooms):
        if (room[0] - 10 <= level <= room[0] + 10) and len(room[1]) < m:
            rooms[index][1].append((level, name))
            flag = False
            break
    if flag:
        rooms.append([level, [(level, name)]])

for room in rooms:
    x, room = room
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print('Started!')
        for each in room:
            print(*each)
    else:
        print('Waiting!')
        for each in room:
            print(*each)
