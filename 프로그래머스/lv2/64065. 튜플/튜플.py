def solution(s):
    result = []
    process = []
    s = s.strip("{}")
    s = s.split("},{")
    for value in s:
        check = value.split(",")
        check = set(map(int, check))
        process.append(check)
    process.sort(key=lambda x: len(x))

    for index, value in enumerate(process):
        if index == 0:
            result.append(*value)
        else:
            result.append(*(process[index] - process[index-1]))

    return result