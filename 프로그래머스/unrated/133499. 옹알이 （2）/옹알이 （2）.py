def solution(babbling):
    answer = 0
    check = ['aya', 'ye', 'woo', 'ma']

    for bab in babbling:
        for che in check:
            if che*2 not in bab:
                bab = bab.replace(che, " ")
        bab = bab.lstrip(" ")
        bab = bab.rstrip(" ")
        if len(bab) == 0:
            answer += 1
    return answer