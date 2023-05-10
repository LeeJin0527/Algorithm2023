from collections import defaultdict
def solution(participant, completion):
    answer = defaultdict(int)
    for part in participant:
        answer[part] += 1
    for comp in completion:
        answer[comp] += 1
    for ans in answer:
        if answer[ans] % 2 != 0:
            return ans
