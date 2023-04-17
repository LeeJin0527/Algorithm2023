def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key=lambda x: x[1])
    for route in routes:
        start, end = route
        if camera < start:
            answer += 1
            camera = end
    return answer