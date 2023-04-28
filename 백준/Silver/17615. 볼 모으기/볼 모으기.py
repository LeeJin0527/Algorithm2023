n = int(input())
balls = input().rstrip()
count = []
rightSideRedBalls = balls.rstrip('R')
count.append(rightSideRedBalls.count('R'))

rightSideBlueBalls = balls.rstrip('B')
count.append(rightSideBlueBalls.count('B'))

leftSideRedBalls = balls.lstrip('R')
count.append(leftSideRedBalls.count('R'))

leftSideBlueBalls = balls.lstrip('B')
count.append(leftSideBlueBalls.count('B'))
print(min(count))