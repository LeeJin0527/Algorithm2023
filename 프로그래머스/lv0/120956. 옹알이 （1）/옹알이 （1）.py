def solution(babbling):
    result = 0
    tmp = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        for t in tmp:
            bab = bab.replace(t, " ", 1)
        if len(bab.rstrip()) == 0:
            result += 1
    
    return result