def solution(N, number):
    answer = 0
    check = set()
    dic = dict()
    check.add(0)
    for index in range(1, 9):
        num = int(index * str(N))
        if num == number:
            return index
        check.add(num)
        dic[index] = [num]

    for index in range(2, 9):
        for j in range(1, index):
            k = index - j
            for eachJ in dic[j]:
                for eachK in dic[k]:
                    temp = [eachJ + eachK, abs(eachJ - eachK), eachJ // eachK, eachJ * eachK]
                    for tem in temp:
                        if tem in check:
                            continue
                        if tem == number:
                            return index
                        dic[index].append(tem)
                        check.add(tem)
    return -1