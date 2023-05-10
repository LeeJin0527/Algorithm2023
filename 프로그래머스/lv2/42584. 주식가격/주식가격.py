from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        check = prices.popleft()
        sec = 0
        for price in prices:
            sec += 1
            if price < check:
                break
        answer.append(sec)
    return answer