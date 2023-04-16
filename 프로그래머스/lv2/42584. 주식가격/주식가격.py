from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        x = prices.popleft()
        cnt = 0
        for price in prices:
            if price >= x:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer