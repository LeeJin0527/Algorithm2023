n = int(input())
balls = input().rstrip()

moveCount = []

rightSideRedBallAssemble = balls.rstrip("R")
moveCount.append(rightSideRedBallAssemble.count('R'))

rightSideBlueBallAssemble = balls.rstrip("B")
moveCount.append(rightSideBlueBallAssemble.count('B'))

leftSideRedBallAssemble = balls.lstrip("R")
moveCount.append(leftSideRedBallAssemble.count('R'))

leftSideBlueBallAssemble = balls.lstrip("B")
moveCount.append(leftSideBlueBallAssemble.count('B'))

print(min(moveCount))