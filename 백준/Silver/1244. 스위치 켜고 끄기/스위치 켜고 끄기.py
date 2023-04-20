n = int(input())
switches = [0] + list(map(int, input().split()))
student = int(input())
for _ in range(student):
    status, start = map(int, input().split())
    if status == 1:
        for k in range(start, len(switches), start):
            if switches[k] == 0:
                switches[k] = 1
            else:
                switches[k] = 0
    elif status == 2:
        if switches[start] == 0:
            switches[start] = 1
        else:
            switches[start] = 0
        for k in range(1, len(switches)):
            if start - k > 0 and start + k < len(switches):
                if switches[start-k] == switches[start + k]:
                    if switches[start - k] == 0:
                        switches[start-k] = 1
                        switches[start + k] = 1
                    elif switches[start - k] == 1:
                        switches[start - k] = 0
                        switches[start + k] = 0
                else:
                    break
switches = switches[1:]
for index, value in enumerate(switches):
    if index % 20 == 0 and index != 0:
        print()
    print(value, end = ' ')
