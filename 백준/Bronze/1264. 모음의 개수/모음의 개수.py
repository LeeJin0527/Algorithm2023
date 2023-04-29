while True:
    check = input().rstrip()
    if check == "#":
        break
    check = list(check)
    cnt = 0
    for che in check:
        che = che.lower()
        if che == 'a' or che == 'e' or che == 'i' or che == 'o' or che == 'u':
            cnt += 1
    print(cnt)