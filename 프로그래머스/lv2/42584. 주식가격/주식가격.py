from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        x = prices.popleft()
        cnt = 0
        for value in prices:
            if x > value:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer