p, m = map(int, input().split())
people = []
for _ in range(p):
    level, name = input().rstrip().split()
    people.append([int(level), [int(level), name]])
rooms = []
for person in people:
    flag = True
    for index in range(len(rooms)):
        if len(rooms[index][1]) == m:
            continue
        if rooms[index][0] - 10 <= person[0] <= rooms[index][0] + 10:
            rooms[index][1].append(person[1])
            flag = False
            break
    if flag:
        rooms.append([person[0], [person[1]]])
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
