from collections import deque
t = int(input())
for _ in range(t):
    students = list(map(int, input().split()))
    student = students[0]
    students = students[1:]
    sortedStudents = deque()
    sortedStudents.append(students[0])
    students = deque(students[1:])
    answer = 0
    while students:
        x = students.popleft()
        if x > sortedStudents[-1]:
            sortedStudents.append(x)
        else:
            check = 0
            count = len(sortedStudents)-1
            while sortedStudents[count] > x and count >= 0:
                count -= 1
                check += 1
            answer += check

            sortedStudents.insert(count+1, x)
    print(f'{student} {answer}')