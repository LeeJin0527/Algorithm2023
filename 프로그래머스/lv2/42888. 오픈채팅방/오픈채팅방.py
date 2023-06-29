from collections import defaultdict
def solution(record):
    answer = []
    check = {}

    for index, rec in enumerate(record):
        reco = rec.split()
        if len(reco) == 3:
            status, uuid, nickName = reco[0], reco[1], reco[2]
            if status == 'Enter':
                check[uuid] = nickName
            elif status == 'Change':
                check[uuid] = nickName

    for i in range(len(record)):
        rec = record[i].split(" ")
        if len(rec) == 3:
            status, id_, nickName = rec[0], rec[1], rec[2]
        else:
            status, id_ = rec[0], rec[1]
            
        if status == 'Enter':
                answer.append(f'{check[id_]}님이 들어왔습니다.')
        elif status == 'Leave':
            answer.append(f'{check[id_]}님이 나갔습니다.')
            
    return answer