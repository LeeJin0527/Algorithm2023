from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        x = prices.popleft()
        count = 0
        for check in prices:
            count += 1
            if x > check:
                break
        answer.append(count)
    return answer
