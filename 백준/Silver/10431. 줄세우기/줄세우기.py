from collections import deque
t = int(input())
for _ in range(t):
    answer = 0
    numbers = list(map(int, input().split()))
    case = numbers[0]
    numbers = deque(numbers[1:])
    sortedStudents = deque()
    firstStudent = numbers.popleft()
    sortedStudents.append(firstStudent)
    while numbers:
        checkNumber = numbers.popleft()
        if checkNumber > sortedStudents[-1]:
            sortedStudents.append(checkNumber)
        else:
            index = len(sortedStudents)-1
            count = 0
            while sortedStudents[index] > checkNumber and index >= 0:
                index -= 1
                count += 1
            sortedStudents.insert(len(sortedStudents) - count,  checkNumber)
            answer += count
    print(f'{case} {answer}')