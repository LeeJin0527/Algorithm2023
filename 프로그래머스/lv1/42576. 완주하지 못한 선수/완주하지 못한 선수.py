from collections import defaultdict
def solution(participant, completion):
    
    participantsDic = defaultdict(int)
    
    for index in range(len(completion)):
        participantsDic[participant[index]] += 1
        participantsDic[completion[index]] += 1
    participantsDic[participant[-1]] += 1
    
    for participants in participantsDic:
        if participantsDic[participants] % 2 == 1:
            return participants