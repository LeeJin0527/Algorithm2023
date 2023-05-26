from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        x = prices.popleft()
        cnt = 0
        for each in prices:
            if x > each:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    
    return answer