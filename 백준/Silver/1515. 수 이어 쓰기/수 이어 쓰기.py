target = input().rstrip()
cnt = 0
while True:
    cnt += 1
    check = str(cnt)
    while len(check) > 0 and len(target) > 0:
        if check[0] == target[0]:
            target = target[1:]
        check = check[1:]
    if len(target) == 0:
        print(cnt)
        break