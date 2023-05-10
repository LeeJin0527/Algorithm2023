def solution(nums):
    n = len(nums)
    check = set(nums)
    if len(check) >= n // 2:
        return n // 2
    return len(check)
    