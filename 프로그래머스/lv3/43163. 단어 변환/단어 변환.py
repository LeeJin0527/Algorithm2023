from collections import deque
def can_change(start, end):
    cnt = 0
    for index, value in enumerate(start):
        if value != end[index]:
            cnt += 1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0])
    while q:
        x, cnt = q.popleft()
        for word in words:
            if can_change(x, word):
                if word == target:
                    return cnt + 1
                else:
                    q.append([word, cnt+1])
            
    return answer