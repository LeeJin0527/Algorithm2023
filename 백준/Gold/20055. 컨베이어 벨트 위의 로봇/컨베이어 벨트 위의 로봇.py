n, k = map(int, input().split())
lst = list(map(int, input().split()))
robot = [0] * n

def move(last, bot):
    for i in range(len(bot)-2, -1, -1):
        if last[i+1] > 0 and bot[i] != 0 and bot[i+1] == 0:
            bot[i+1] = bot[i]
            bot[i] = 0
            last[i+1] -= 1
        bot[-1] = 0
    return last, bot


time = 0

while True:
    if lst.count(0) >= k:
        break
    # 벨트, 로봇 회전
    belt = [lst[-1]] + lst[:-1]
    robot_tmp = [robot[-1]] + robot[:-1]
    lst = belt
    robot = robot_tmp
    robot[-1] = 0


    lst, robot = move(lst, robot)
    if lst[0] > 0:
        robot[0] = 1
        lst[0] -= 1

    time += 1
print(time)