def solution(a, b, n):
    answer = 0

    while True:
        share = int(n / a)
        answer += b * share
        remainder = n % a
        
        n = b * share
        n += remainder
        if n < a:
            break
        if n == a:
            answer += 1
            break

    return answer