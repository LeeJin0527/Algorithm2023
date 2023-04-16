def solution(nums):
    check = set(nums)
    if len(check) >= len(nums) // 2:
        return len(nums) // 2
    return len(check)