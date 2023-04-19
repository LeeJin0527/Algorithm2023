def check(checkWord):
    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    cnt = 0
    for check in checkWord:
        if check == 'a' or  check == 'e' or check == 'i' or check == 'o' or check == 'u':
           cnt += 1
    if cnt == 0:
        return False
    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(0, len(checkWord)-2):
        temp = checkWord[i: i+3]
        vowel, consonant = 0, 0
        for tem in temp:
            if tem == 'a' or tem == 'e' or tem == 'i' or tem == 'o' or tem == 'u':
                vowel += 1
            else:
                consonant += 1
        if vowel >= 3 or consonant >= 3:
            return False
    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(0, len(checkWord)-1):
        temp = checkWord[i: i+2]
        if len(temp) >= 2:
            if temp[0] == temp[1]:
                if (temp[0] == 'e' and temp[1] == 'e') or (temp[0] == 'o' and temp[1] == 'o'):
                    continue
                return False
    return True



while True:
    word = input().rstrip()
    if word == 'end':
        break
    if check(word):
        print("<"+word+">", "is acceptable.")
    else:
        print("<"+word+">", "is not acceptable.")