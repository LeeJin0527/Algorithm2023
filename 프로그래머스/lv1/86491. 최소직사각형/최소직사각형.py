def solution(sizes):
    answer = 0
    width, height = [], []
    for size in sizes:
        size.sort()
        width.append(size[0])
        height.append(size[1])
    return max(width) * max(height)