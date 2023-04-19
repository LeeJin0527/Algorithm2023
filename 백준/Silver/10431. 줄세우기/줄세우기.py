import copy
n = int(input())
for t in range(1, n+1):
    lst = list(map(int, input().split()))
    students = lst[1:]
    temp = copy.deepcopy(students)
    check = students.sort()
    left = [temp[0]]
    right = temp[1:]
    checkCnt = 0
    result = 0
    if temp == students:
        print(t, 0)
        continue
    for each in right:
        if each > left[-1]:
            left.append(each)
            continue
        tempCnt = 0
        for i in range(len(left)):
            if left[i] > each:
                break
            tempCnt += 1
        result += len(left) - tempCnt
        left.insert(tempCnt, each)
    print(t, result)