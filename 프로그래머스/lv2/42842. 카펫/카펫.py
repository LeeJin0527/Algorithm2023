def solution(brown, yellow):
    answer = []
    n = brown + yellow
    for height in range(3, n+1):
        if n % height == 0:
            width = int(n / height)
            if (height - 2) * (width - 2) == yellow:
                if height > width :
                    return [height, width]
                else:
                    return [width, height]
