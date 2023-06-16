def solution(new_id):
    answer = ''
    new_id1 = new_id.lower()

    new_id2 = ''
    for new in new_id1:
        if (ord(new) < 97) or (ord(new) > 122):
            if not (str(0) <= new <= str(9)):
                if not ( new == '-' or new == '_' or new == '.') :
                    continue
        new_id2 += new
    while True:
        flag = False
        new_id3 = new_id2.replace("..", ".")
        for index in range(len(new_id3) - 1):
            if new_id3[index] == '.' and new_id3[index+1] == '.':
                flag = True
        if flag == False:
            break
        new_id2 = new_id3
    new_id4 = new_id3.lstrip(".")
    new_id4 = new_id4.rstrip(".")
    
    if len(new_id4) == 0:
        new_id4 = 'a'

    if len(new_id4) >= 16:
        new_id4 = new_id4[:15]
        new_id4 = new_id4.rstrip(".")

    elif len(new_id4) <= 2:
        check = new_id4[-1]
        while True:
            if len(new_id4) == 3:
                break
            new_id4 += check

    return new_id4