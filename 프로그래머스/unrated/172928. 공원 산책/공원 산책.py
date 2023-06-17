def solution(park, routes):
    answer = []
    for a in range(len(park)):
        for b in range(len(park[0])):
            if park[a][b] == 'S':
                locationX, locationY = a, b
    di = ['E', 'N', 'S', 'W']
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]
    for route in routes:
        originX, originY = locationX, locationY
        direction, cnt = route.split(" ")
        cnt = int(cnt)
        idx = di.index(direction)
        nx = locationX + (dx[idx] * cnt)
        ny = locationY + (dy[idx] * cnt)
        if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
            continue
        for _ in range(cnt):
            nx = locationX + dx[idx]
            ny = locationY + dy[idx]
            if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                nx = originX
                ny = originY
                break
            if park[nx][ny] == 'X':
                nx = originX
                ny = originY
                break
            locationX, locationY = nx, ny
        locationX, locationY = nx, ny

    return [locationX, locationY]