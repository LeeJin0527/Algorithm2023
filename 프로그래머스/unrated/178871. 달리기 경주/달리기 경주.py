def solution(players, callings):
    rankDic = dict()
    playersDic = dict()
    for index, value in enumerate(players):
        rankDic[index+1] = value
        playersDic[value] = index+1

    for index, value in enumerate(callings):
        cur_index = playersDic[value]
        pre_index = cur_index - 1
        playersDic[rankDic[cur_index]], playersDic[rankDic[pre_index]] = playersDic[rankDic[pre_index]], playersDic[rankDic[cur_index]]
        rankDic[cur_index], rankDic[pre_index] = rankDic[pre_index], rankDic[cur_index]

    return list(rankDic.values())